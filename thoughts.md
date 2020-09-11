#project

## Face ID - Facial Recognition Security System
### What is needed
- Need to design a system which can capture the face of the person and then infer the Age, Gender, Time. 
- Sends the notification to the owner of the security system with details and also store in the database with an entry of the visit and person details with image.


### Thoughts
- Can have system in two parts since we need to capture the image and also then run a deep learning based inference pipeline
- One part is for capture of the image and another for the inference and the post processing and other logic.
- system1 will capture the image and system2 will perform the post processing.
- system1 has to transfer the image of the person and the current time to the system2.
- system1 need a camera system, no need for higher DMIPS since we don't need to perform any image processing.
- system2 should have enough DMIPS or GFLOPS to run a image processing and deep learning based inference pipeline for the person details from the image.
- Both system1 and system2 should be connected such that system1 can transfer the image to system2.
- system2 can in-turn send commands to system1 for taking actions based on the feedback from the user in case user acknowledges the person and allow the person to enter. system1 in this case can take case of the security systems.
- The mode of transport can be wired or wireless. Wired will be the Ethernet connection and wireless can be the Bluetooth or WiFi.


- system1 be a nodemcu and system2 as raspberrypi3
- system1 as raspberrypi3 and system2 as Nvidia Jetson Nano.


### System1
- Low computing board
- Camera connected
- Image sharing pipeline to system2
- Client to accept the commands from the system2
- Control Systems connected.

### System2
- Moderate to high computing power 
- Image processing and Deep learning inference pipeline
- Client for the Image receiving from system1.
- Control unit for the User notification based on the image/face recognition.
- Receive inputs from the User via some mechanism.

---

### Need to Decide
- **system1** be a **nodemcu** and **system2** as **raspberrypi3** or **system1** as **raspberrypi3** and **system2** as **Nvidia Jetson Nano**.
- Which **messaging framework** between the system1 and system2.
- Which **communication protocol** for the communication, which can serve both the image transfer and the messaging. Should these be different methods for the reliability. Need to check.
- Decide on the **camera specs** to capture the image. 
- Shall complete image processing should be done on the system2 or something can also happen on the system1. In case if the face is not properly captured then system1 should capture the image again and for this the face detection shall happen on the system1 and later the face recognition can happen on the system2.
- **Programming language**. Since the system1 and system2 are very low on resources then language should be the** c/c++** or **rust** or **lua**(may be, need to check if this can be faster to program and also provide the necessary speed at the system1). In case if the image processing needs to happen at the system1 then we need to check is the face recognition algorithm can used from opencv or dlib3 or from scratch. Right now with this the possible system can be RPi3 and Jetson Nano. Lets see.
- **Framework** for the deep learning and image processing.
- Data path for image transfer can be the WiFi or Bluetooth and for commands it can use MQTT. (https://www.hackster.io/ruchir1674/raspberry-pi-talking-to-esp8266-using-mqtt-ed9037)

--- 

### Decided
- I have decided to go with system1 as RPi3 and system2 as Nvidia Jetson Nano.
	- Main reason is because this project has some new things which i will be learning along the way and I dont want a resource constraint system to battle at two fronts - learning new thing and also squeeze the performance which will take some good enough command on those new skills. May be later we can change the system and then optimize the systems to run on the new boards.
	- Another reason is that system1 will be doing some image processing in form of **face detection** atleast so that it can at its level decide it the face is captured properly or not. Once the proper face is detected than it can transmit that face image to the system2.
	- system2 will be running a deep learning pipeline and it should be capable to run the CPU/GPU intensive tasks. And for this right now Nvidia Jetson Nano is the right fit. Not sure how RPI3 will fit here. But I will definitely check this out later.

---

### How the system will function on high level
- system1 captures the image. Detects the face. Transmits to the system2 and waits for the response. This cycle will make the single transaction. 
	- Its possible that in single transaction there can be multiple face images. Because there are more than 1 person at the entrance.
- system2 receives the face image and then it performs the face recognition biometrics for Age, Gender, also matches the face with the stored faces in the database for known person.
- system2 will notify the user of this event with some details and wait for the user for some feedback like deny the entry or give the entry or its also possible that if the person is known and the user already granted the access which is stored in the metadata of the face image in the database then it will just notify the user and will not wait for the feedback from the user.

---

Concise Binary Object Representation (CBOR) is a binary data serialization format loosely based on JSON. https://en.wikipedia.org/wiki/CBOR


### Start with this
- Face recognition and detection on the raspberrypi with OpenCV and Dlib.
- Check the performance of the model and check the DMIPS required
- Implement a interfacing between the two boards for data and control channel

