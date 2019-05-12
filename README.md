# SG5238 Architecting IOT Solutions CA2

## Implementing emotion detection for driver safety

Using the Movidius NCS to perform analysis of webcam streams on edge devices to detect road rage.

When a driver is detected to be consistently angry over a period of time, calming music is played to reduce the driver's anger.

## Instructions
1. Clone the repository from Github
   ``` bash
   git clone https://github.com/bengohyp/sg5238.git
   ```
1. Make sure your webcam and Movidius stick is connected to your computer. (optional) You can test the Movidius stick by opening terminal and executing 
   ```
   make test-ncs
   ```
1. (optional) If you do not have a Modivius NCS, you can test the webcam by opening terminal and executing 
   ```
   make test-run
   ```
1. To run the application, open a terminal and execute 
   ```bash
   make run
   ```
1. When the application is running, you should see a window displaying the webcam image. A red bounding box shows any faces that are detected by the webcam. The NCS will infer the face's emotion.
1. If the confidence of the inferred emotion is over a set threshold, it will be added to a moving window.
1. When all elements of the moving window is "angry", music will be played in the backround to calm the driver down.

## Known Bug
- When executing ```make run```, a ```NameError: name 'img' is not defined``` error might sometimes appear. To resolve this error:
1. Comment the line that is causing error
   ```python
   # img = cv2.resize(img, (NETWORK_HEIGHT, NETWORK_WIDTH))
   ```
   and execute ```make run```. This will give an error
   ```
   graph.queue_inference_with_fifo_elem(fifo_in, fifo_out, img.astype(numpy.float32), None)
   ```
1. Uncomment the line that was causing error
   ```python
   img = cv2.resize(img, (NETWORK_HEIGHT, NETWORK_WIDTH))
   ```
   and execute ```make run``` again.

## Project Deliverables

- [ ] 1 Report in .docx or .pdf format
- [ ] 1 softcopy of source code in GitHub
- [ ] 1 page PPT advertisement
    \- Suggest using [___Canva___](https://www.canva.com/) to design the advertising poster
- [ ] 1 demo video on YouTube demonstrating source code
- [ ] 1 zip file containing all documents

Submission deadline: __30 May 2019 23:59hrs__

Return MVNCS on __19 June 2019__