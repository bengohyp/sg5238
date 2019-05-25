# SG5238 Architecting IOT Solutions CA2

# Implementing emotion detection for driver safety

This project aims to use the Movidius NCS to perform analysis of webcam streams on edge devices to detect road rage. When a driver is detected to be consistently angry over a period of time, calming music is played to reduce the driver's anger.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need:
- VirtualBox
- Ubuntu 16.04 ISO
- Intel® Movidius™ Neural Compute Stick (NCS)

### Installing

1. Install VirtualBox and create a new virtual machine with the Ubuntu 16.04 ISO. Instructions on how to set up a can be found [here](https://itsfoss.com/install-linux-in-virtualbox/).
1. After starting up the VM, start a terminal instance by pressing `Ctrl+Alt+T` on the keyboard.
1. In the terminal, execute these commands to install pip.
   ```bash
   cd ~ # navigate to the user's home directory
   mkdir workspace # create a directory named 'workspace'
   cd workspace # navigate to the 'workspace' directory
   sudo apt install python-pip # install pip
   ```
1. Virtualenv is a tool to create isolated Python environments as best practice. Execute these commands to set up a virtualenv for this project.
   ```bash
   pip install virtualenv # install virtualenv
   virtualenv env # create a new virtual environment for our project
   source env/bin/activate # activate the newly created virtual environment
   ```
1. Execute these commands to install the Intel® Movidius™ SDK
   ```bash   
   sudo apt-get install git # install git
   git clone -b ncsdk2 http://github.com/Movidius/ncsdk && cd ncsdk && make install # install the movidius sdk
   ```
1. Execute these commands to extract our source code and install the required dependencies (this step takes ~15mins to complete)
   ```bash
   cd .. # navigate back to the 'workspace' directory
   unzip sg5238.zip # unzip our project source code
   cd sg5238 # navigate to the sg5238 directory
   pip3 install -r requirements.txt # install dependencies
   ```

## Testing the hardware

7. Ensure that the Intel® Movidius™ NCS is plugged in and recognised by the VM. To test if the NCS is connected, run:
   ```bash
   make test-ncs # run hello_ncs_py example
   ```

## Running the application

8. If the above test is successful, run the application with:
   ```bash
   make run # run the application
   ```
   A window showing the webcam output will appear on screen. In the terminal, an array of inference results will be printed. 

### Inference results

9. When the array results consist entirely `'angry'` inferences, music will be played in the background for 30 seconds. 
10. At any time, you can press the `q` key to stop the application.


# 

https://movidius.github.io/ncsdk/vm_config.html

## Instructions (Renjie)
1. Clone the repository from Github
   ``` bash
   git clone https://github.com/bengohyp/sg5238.git
   ```
1. Ensure your environment is right. There are two methods to do so:
    1. by [Anaconda](https://anaconda.org/anaconda/python)
    ```bash
    cd sg5238
    conda env create -f=environment.yml
    source activate emo_detect
    ```
    2. by native pip (get [Python](https://www.python.org/downloads/))
    ```bash
    cd sg5238
    python -m venv env # Creates virtual environment
    source env/bin/activate
    pip install -r requirements.txt
    ```
1. Get Intel® Movidius™ Neural Compute SDK
 ```bash
 git clone -b ncsdk2 http://github.com/Movidius/ncsdk && cd ncsdk && make install
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

## Known Bug (fixed)
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

- [x] 1 Report in .docx or .pdf format
- [ ] 1 softcopy of source code in zip file
- [x] 1 page PPT advertisement
    \- Suggest using [___Canva___](https://www.canva.com/) to design the advertising poster
- [x] 1 demo video on YouTube demonstrating source code
- [ ] 1 zip file containing all documents

Submission deadline: __30 May 2019 23:59hrs__

Return MVNCS on __19 June 2019__