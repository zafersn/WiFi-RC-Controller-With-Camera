# RASPBERRY PI- ARDUINO ANDROID-CONTROLLED RC-CAR ROVER WITH LIVE VIDEO STREAMING
# ----------------------------- Pi_CAR -----------------------------
[![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V1Images/images/yotubeT1.png)](https://youtu.be/J8r_bX_RNzU)

## Materials
<br>

Product Name| Piece
----| ---- 
Arduino Nano / UNO / Mega| 1
Raspberry Pi| 1
Raspberry Pi Camera Module| 1
Wi-Fi Dongle| 1
L298N,BTS7960,L293 Motor Drive| 1 or 2 
DC MOTOR|  2  or   4
12V Lipo Battery| 1
Jumper Cables | ~
Vehicle Chassis | 1
<br>


## Arduino:
### PURPOSE AND TASKS:

*	Arduino was used for motor control.
* Arduino and Raspberry Pi were connected by serial communication.
* Before PWM signal interval which will be sent from Android phone to Arduino don't transfer, this signal was calculated. (Because of the next updates and easily interfere to PWM variable by users.)
* The Raspberry Pi provides the Wi-Fi communication with Arduino and the user (Android phone).
* In the following section, we show the circuit schematic for Raspberry Pi, Raspberry Pi Camera, Arduino, L298N Motor Driver, motors and batteries.
 

### SETTING UP ARDUINO AND PIN CONNECTION SCHEMATIC

* Data which come to Arduino is sent as a PWM interval that go to the motors directly. There are two values `+ (forward)` or `- (backward)` for decide direction with PWM value.
* Above-mentioned situations is considered by us, there can be made various modifications.
* PWM interval is between` 0-255.`
* RIGHT AND LEFT motor PWMs' and servo motor angle is taken as a String(e.g. `200:200!888`) from phone. This String value is splitted with `:` and `!` characters and created the array that has 3 elements.
* The value after the `!` character is the servo motor's angle value which connected with camera. Servo motor is not used in this project.
 **Motor Moving, PWM data and situations of the car**<br>
Example:<br>
 0:0 //stop<br>
 200:200 // move forward. (2 motors work with 200pwm)<br>
 200:-200 //move backward. (2 motors work with 200pwm)<br>
 200:-200 // left motor turns 200 pwm to forward, right motor turns 200 pwm to backward (The car turns its around from left to right.)<br>
 200:-200 // left motor turns 200 pwm to backward, right motor turns 200 pwm to forward (The car turns its around from right to left.)<br>
 200:100 // The car moves as turning to the right.<br><br>
 




[![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V1Images/images/youtbeT2.png)](https://youtu.be/D4ewbO-OGLY)
<p align="center"> <b>L298 - Dual Full Bridge Driver</b>
<img src="https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V1Images/images/wificontrol.png"  />
</p>
<p align="center"> <b>BTS7960 - 43A MOTOR DRIVE</b>
<img src="https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images//images/BTS7960%20fritzing2.png"  />
</p>


<br><br>
* Connections among Arduino, Raspberry pi,Raspberry pi camera module, L298N motor driver, Motors and Power Supply are set up as above picture.
* After connected Arduino pins and Raspberry pi as above picture, we can load our codes to Arduino. That do by this sequence:
* Detail information about Arduino codes is placed in that codes.
*  [**Download**](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/tree/master/ENGLISH/V2/androidToRaspberryEnglishInformation)  `androidToRaspberry.ino` file and open the this file with double click.
* For uploading that project file to Arduino, first you must select the Arduino model from `Tools => Board` menu.<br><br>


![Screen Shot RA1](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V1Images/images/ra1.png)
<br><br>
* Again from `Tools` menu, you must show which port plugged to Arduino board. `Tools => port`
* After realize all steps, now you can upload the codes to Arduino board. You can complete the uploading process by pressing `Upload` button from left-up corner of the program.<br><br><br>
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V1Images/images/ra2.png)
<br><br>
## RASPBERRY PI:
### PURPOSE AND MISSIONS:

* Taking video stream with Raspberry Pi camera module and trasfer that stream to phone via Raspberry pi.
* Connection between Arduino and Android phone.

### RASPBERRY PI SETUP:
Raspberry pi setup is quite simple. First, <br>
Win32DiskImager is the program that is required to print the operating system to the SD card.  [**Click**](http://www.gezginler.net/indir/win32-disk-imager.html) to download

## 1. Raspbian Operating System Downloads;
We will need to write the  the   operating system containing vehicle control software.The point to be noted here is that when selecting the operating systems listed below, download it according to the Wi-Fi module in your hand and print it to the sd card.Modems supported by Operating Systems and Operating Systems are given below.
<br>
### Downloadable operating system for Raspberry Pi 3
We have 2 alternative methods for Raspberry pi 3;<br>

1. Using built-in Wi-Fi directly on Raspberry Pi. <br>
2. Using an external USB Wifi adapter.(It is the recommended method for distance and data speed. Of course this will vary depending on the Wi-Fi adapter you use.)
<br>

### 1.If you want to manage Pi_CAR via Raspberry pi 2 or  the built-in Wi-Fi module on the Raspberry Pi 3.Download the operating system on [**this link**](https://drive.google.com/open?id=0B6yjwSAqPTgfdEV1eTlfZ0lVbW8)  and print to the SD card.



### 2.If you want to manage Pi_CAR by using Wi-Fi module externally mounted on raspberry pi 3. Download the operating system on [**this link**](https://drive.google.com/file/d/0B6yjwSAqPTgfYkhxWEN2dXBIQlU/view?usp=sharing)  and print to the SD card.



Wi-Fi devices and chipsets we have available and tested for this option  
<br> Hangisini kullanayım sülo <br>
For this option, we have avaible and tested wifi devces and chipsets.
<br>

Tested Devices|Chipsets
---------- | --------
Dark WDN300A5 | RTL8192CU
Tenda UH150 | RT2870/RT3070
AWUS036NH | RT2870/RT3070
<br>

Detailed information for other supported chipsets and devices:http://elinux.org/RPi_USB_Wi-Fi_Adapters

## 2. Printing Operating System to Micro-SD Card
We extract the downloaded image file from within the zip.Then we open the Win32DiskImager program we downloaded earlier. We choose our img file from the specified location.

![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/win32diskimager.jpg)

Once you are sure your Sd card is connected to the computer, you can see it in the Devices section. Then click on the write button and start burning. The writing process takes about 5-7 minutes. The completion of the writing process is indicated by the newly opened window "Write Successfull." Wait until you see the article.


![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/Write%20Succesful.png)
## 3.Connections and Operation

After the writing process is completed, you can remove your SD card from the computer and insert it into the Raspberry.
All you need to do now is mount the Arduino to Raspberry via USB and mount it after you have made the necessary power and motor drive connections.
<br>
Video description:
<br>
[![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/youtube%20play2.png)](https://youtu.be/yNLug0DhQlc)

## ANDROID:

### PURPOSE AND MISSIONS:
* Maintaining control of RC-Car that made from Android and Raspberry Pi.<br>
* Simple and pure design for user.<br>
* Taking video stream via Raspberry Pi and show this to user.<br>

### INSTALL ANDROID APPLICATION:
*  Installing of the application is very simple. Only after enter the **ANDROID GOOGLE PLAY** market, you can type in searching box `com.stackcuriosity.tooght` or application name `RC CONTROLLER WITH CAMERA` for directly access to application.<br><br>

<p align="center">
 <a href="https://play.google.com/store/apps/details?id=com.stackcuriosity.tooght"><img src="https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/Google.png"/></a>
</p>
### USING THE APPLICATION AND HINTS
#### Raspberry Pi Connection Informations

Once you've downloaded your Android app, you will see the following welcome : Now all you need to do is check the tool. screen.<br>
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/Screenshot_20161208-155537.png)
<br>
Let's briefly explain the working principle and the introduction of the application.
#### APPLICATION DETAILS

##### 1. EXPLAINING OF THE VISUAL DESIGN AND PROGRAMMING LOGIC
**Our application rely on 4 basis. These are;**<br><br>
 I. Provide direction control of the car.<br>
 II. Transfer live video streaming from car to user.<br>
 III. Connection signal level indicator of vehicle.<br>
 IV. Follow Me (Vey Soon). (Following the car its owner.)<br>
 
 * To that 4 basis;
* Main details using direction control of the car was told in `Arduino` section. If we explain to the Android side, there will be available `Seek bar (Velocity setting)`, `Camera On / Off`,`Wi-Fi status indicator` and `Arrow keys`.<br><br> ![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/Screenshot_description_en.png)<br><br>

* **Seek bar(Velocity setting)**is created from 15 slice and velocity coefficient is 17. So any move of the Seek bar, there will be changing 17 and its multiples. For instance, If Seek bar in fifth order, produced pwm = 5*17 = 85.

* **Menu keys (Camera On/Off and WiFi Indicator)** Other vehicle control functions beside Seekbar 'ın;<br> Camera on / off button for taking the camera image through the vehicle " ![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/ic_eye.png) `Open` ", " ![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/ic_eye_off.png) `CLOSE` ", In the same way, an indication of whether our application is connected to the Wi-Fi network we created on Raspberry Pi."<br> ![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/ic_wifi_on.png) `NOT CONNECTED` ", "![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/ic_wifi_off.png) `CONNECTED` "

* **Arrow keys** provide seperating directions of data which take from Seek bar(Velocity setting). For moving direction of the car, `+` or `-` sign come to head of the PWM value.<br>
**For example:**

 200:200 // move forward. (2 motors work with 200pwm)<br>
  200:-200 //move backward. (2 motors work with 200pwm)<br>
 200:-200 // left motor turns 200 pwm to forward, right motor turns 200 pwm to backward (The car turns its around from left to right.)<br>
 200:-200 // left motor turns 200 pwm to backward, right motor turns 200 pwm to forward (The car turns its around from right to left.)<br>
 200:100 // The car moves as turning to the right.<br><br>

#### **2.SENSITIVITY IN TURNING LEFT AND RIGHT**
 * When our car moving to right cross and left cross, motors' PWM value which will be turning side decreases, and so this provides slower motor rotating. So, the car can achieve the intended turnings. **This rotating sensitivity setting let to user.**<br>
* The formula for calculating cross turnings: **PWM VALUE - ((PWM VALUE) / PWM RATE)**<br>
* In default, PWM RATE is `2`.<br>
* You can reach the PWM RATE setting from right-top button in the screen and from there to `Settings` menu.<br><br>
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V1Images/images/Screenshot_20160713-205757.png)<br>![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V1Images/images/Screenshot_20160713-205807.png)<br><br>

*  PWM interval which can be entered is a value as a **minimum and maximimum between 1-4 interval in integer and double type**.<br><br>
 


### ICON OF OUR APPLICATION:

![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V1Images/images/raspi_car.png)




## TEST VIDEO:
[![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V1Images/images/testvd1.png)](https://youtu.be/qbkH2KFcKqw)
[![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/play_video2.png)](https://youtu.be/CT-hgXIPRIk)<br><br>




-------------------------------------------------------------------------------------
<br><br>
#<p align="center"> <b>BRIEF AND ABSTRACT INSTALLATION</b></p>
<br><br>
<p align="center"> <b>FOR DETAIL INFORMATION AND INISTALLATION DETAILS, PLEASE START AT THE TOP OF THE PAGE.!!</b>
<img src="https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images//images/raw.gif" alt="DETAYLI ANLATIM VE KURULUM" align="middle" />
</p>

## **STEP 1:**
<br>
1.If you want to manage Pi_CAR via Raspberry pi 2 or  the built-in Wi-Fi module on the Raspberry Pi 3.Download the operating system on [**this link**](https://drive.google.com/file/d/0B6yjwSAqPTgfX1dsaVVJZThEN2c/view?usp=sharing)  and print to the SD card.
<br>

2.If you want to manage Pi_CAR by using Wi-Fi module externally mounted on raspberry pi 3. Download the operating system on [**this link**](https://drive.google.com/file/d/0B6yjwSAqPTgfYkhxWEN2dXBIQlU/view?usp=sharing)  and print to the SD card.
<br>

## **STEP 2**
Download the Arduino control software from this  [**link**](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/tree/master/ENGLISH/V2/androidToRaspberryEnglishInformation) and upload to Arduino. 

## **STEP 3**
Download the Android control software from this  [**link**](https://play.google.com/store/apps/details?id=com.stackcuriosity.tooght) and upload to Android Phone. 
<br><br><br>
**And the operation is complete. If you have correctly connected the Arduino motor drivers, you can now start checking the vehicle.**

<p align="center">
 <a href="https://play.google.com/store/apps/details?id=com.stackcuriosity.tooght"><img src="https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images//images/Google.png"/></a>
</p>

