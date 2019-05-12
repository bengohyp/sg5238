import cv2
import numpy
import pygame
import argparse
import face_recognition
import mvnc.mvncapi as mvnc

# Construct the argument parser with default values
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", type=bool, default=False,
                    help="Will not connect to Movidius NCS if test mode is True")
parser.add_argument("-g", "--graph", type=str, default="graph/emotiongraph",
                    help="Path to neural network graph")
ARGS = parser.parse_args()

# Initialize some variables
in_test_mode = ARGS.test
sample_rate = 10
moving_window_size = 10
confidence_threshold = 0.75
count = 1
face_locations = []
past_results = []
process_this_frame = True
NETWORK_HEIGHT = 224
NETWORK_WIDTH = 224
pygame.init()
calm_music = pygame.mixer.Sound("calm_30s.wav")

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Open the enumerated device and get a handle to it
if not in_test_mode:
    # Look for enumerated NCS device(s); quit program if none found.
    devices = mvnc.enumerate_devices()
    if len(devices) == 0:
        print("No devices found")
        quit()
    # Get a handle to the first enumerated device and open it
    device = mvnc.Device(devices[0])
    device.open()

# Load the inference graph file onto the NCS device
if not in_test_mode:
    # Read the graph file into a buffer
    with open(ARGS.graph, mode='rb') as f:
        blob = f.read()

    # Load the graph buffer into the NCS
    graph = mvnc.Graph(ARGS.graph)
    # Set up fifos
    fifo_in, fifo_out = graph.allocate_with_fifos(device, blob)

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        # Get the image box around the detected face
        for (top, right, bottom, left) in face_locations:
            # Scale back up face locations
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            # Get the box around the face
            img = frame[top:bottom, left:right]
        # Resize image [Image size if defined by choosen network, during training]
        img = cv2.resize(img, (NETWORK_HEIGHT, NETWORK_WIDTH))
        # Increment sample_rate for inference
        count += 1
        # Read & print inference results from the NCS
        if not in_test_mode and count == sample_rate:
            labels = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']
            # Load the image as a half-precision floating point array
            graph.queue_inference_with_fifo_elem(fifo_in, fifo_out, img.astype(numpy.float32), None)
            # Get the results from NCS
            output, userobj = fifo_out.read_elem()
            # Find the index of highest confidence
            top_prediction = output.argmax()
            # Get execution time
            # inference_time = graph.get_option(mvnc.GraphOption.RO_TIME_TAKEN)

            # print("I am %3.1f%%" % (100.0 * output[top_prediction]) + " confident you are " + labels[top_prediction] + " ( %.2f ms )" % (numpy.sum(inference_time)))

            if len(past_results) > moving_window_size:
                past_results.pop(0)
            if output[top_prediction] > confidence_threshold:
                past_results.append(labels[top_prediction])

            print(past_results)

            if len(past_results) > moving_window_size - 1:
                if (all(x == "angry" for x in past_results)):
                    if not pygame.mixer.get_busy():
                        channel1 = calm_music.play()
                        print("Road rage detected! Playing calming music in the background")

            # Reset count
            count = 1

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left) in face_locations:
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face ( x1, y1 ) , ( x2, y2 )
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    # Display the resulting image
    cv2.imshow('Emotion Detection with Face Detection', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
