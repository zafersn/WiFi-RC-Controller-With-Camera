# RASPBERRY PI- ARDUINO ANDROID-CONTROLLED RC-CAR ROVER WITH LIVE VIDEO STREAMING
# ----------------------------- Pi_CAR -----------------------------

[![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V1Images/images/yotubeT1.png)](https://youtu.be/J8r_bX_RNzU)
 <p align="center" ><h1>------ CONTENTS ------</h1></p>
 
* USED MATERIALS
* RASPBERRY PI INSTALLATION
* SAMPLE VEHICLE SELECTION AND RASPBERRY PI PIN CONNECTION SCHEME
* ANDROID APPLICATION INSTALLATION AND USER'S GUIDE
* WINDOWS APPLICATION INSTALLATION AND USER'S GUIDE
* TEST VIDEO
* QUICK INSTALLATION

## Used materials
<br>

Product Name| Piece
----| ---- 
Raspberry Pi| 1
Raspberry Pi Camera Module| 1
Wi-Fi Adaptör| 1 (Optional for Pi 3)
L298N,BTS7960,L293,ESC Motor Drive| 1 or 2 
DC MOTOR|  2  or   4
12V Lipo Batarya| 1
Jumper kablo | ~
Vehicle Chassis| 1
5V Power Supply [**(LM2596-ADJ)**](http://www.robotistan.com/mini-ayarlanabilir-3a-voltaj-regulator-karti-lm2596-adj) or [**(2A Mini)**]( http://www.robotistan.com/2a-mini-ayarlanabilir-voltaj-dusurucu-regulator-karti) |1
<br>

## RASPBERRY PI:
### PURPOSE AND MISSIONS:

* We can take a view  with  using the Raspberry pi camera module and transfer it to the phone via raspberry pi.
* Transferring data from the phone or from the computer to the motor drivers.

### RASPBERRY PI SETUP:
Raspberry pi setup is quite simple. First, <br>
Win32DiskImager is the program that is required to print the operating system to the SD card.  [**Click**](http://www.gezginler.net/indir/win32-disk-imager.html) to download

## 1. Raspbian Operating System Downloads;
We will need to write the  the   operating system containing vehicle control software.**The point to be noted here is that when selecting the operating systems listed below, download it according to the Wi-Fi module in your hand and print it to the sd card.**Modems supported by Operating Systems and Operating Systems are given below.
<br>
### Downloadable operating system for Raspberry Pi 3
We have 2 alternative methods for Raspberry pi 3;<br>

1. Using built-in Wi-Fi directly on Raspberry Pi. <br>
2. Using an external USB Wifi adapter.(It is the recommended method for distance and data speed. Of course this will vary depending on the Wi-Fi adapter you use.)
<br>

### 1.If you want to manage Pi_CAR via Raspberry pi 2 or  the built-in Wi-Fi module on the Raspberry Pi 3.Download the operating system on [**this link**](https://drive.google.com/open?id=0B6yjwSAqPTgfcHRRLXYwMHZ6RWs)  and print to the SD card.





For this option, we have avaible and tested wifi devices and chipsets.
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
# Pi_CAR Wi-Fi  Password: TRaspberry

After the writing process is completed, you can remove your SD card from the computer and insert it into the Raspberry.
**All you need to do now is mount the car after you have made the necessary power and motor drive connections to Raspberry.**
<br>

### [Click!](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/ENGLISH/V3/select_Vehicle_en.md) on the sample vehicle selection and the appropriate pin connection of the vehicle. 


## For further information or if you have any questions please do not hesitate to [contact me!](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/issues)

<br>
**Video Description:**
<br><br>
[![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/youtube%20play2.png)](https://youtu.be/yNLug0DhQlc)


## ![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/android-icon32x32.png)   ANDROID:<br> 

### PURPOSE AND MISSIONS:
* Maintaining control of RC-Car that made from Android and Raspberry Pi.<br>
* Simple and pure design for user.<br>
* Taking video stream via Raspberry Pi and show this to user.<br>
* My purpose is to control the vehicle builded by raspberry pi and the camera on it.

### INSTALL ANDROID APPLICATION:
*  Installing of the application is very simple. Only after enter the **ANDROID GOOGLE PLAY** market, you can type in searching box `com.stackcuriosity.tooght` or application name `RC CONTROLLER WITH CAMERA` for directly access to application.<br><br>

<p align="center">
 <a href="https://play.google.com/store/apps/details?id=com.stackcuriosity.tooght"><img src="https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/Google.png"/></a>
</p>
### USING THE APPLICATION AND HINTS

# IMPORTANT NOTE:
After installing our Android app, it is normally necessary to automatically connect to the Wi-Fi network we created on the car.However, in newer versions of Android (5 and up), Android tries to connect to Google's services to increase user experience and prevent them from connecting to captive networks. According to this connection status, it allows or blocks data communication on the Android Wi-Fi network. Due to this situation, the new versions of Android (5 and above) do not allow connection to the Wi-Fi network we created on our car.For detailed information [click here!](http://android.stackexchange.com/questions/100657/how-to-disable-captive-portal-detection-how-to-remove-exclamation-mark-on-wi-fi).<br>
We have 2 Alternative methods for solving this problem.
* **1st METHOD (RECOMMENDED)** 
   * Using Android Studio<br>
 This method assumes that you are an android developer.<br>
    * Download android Studio from [here!]( https://developer.android.com/studio/index.html).
    * After downloading and making the necessary adjustments, you need to activate your phone's developer options;
      * Settings ==> About Your Phone ==> Compile Number 5 times in a row. The Phone will now say that you are a developer.<br>
      In the same way
      * Settings ==> Developer Options ==> Turn on.
      * Settings ==> Developer Options ==> Enable USB debugging
  
 Now, after you make sure that your phone is connected to the computer and that the phone is recognized by the computer (install the drivers if the phone is not recognized by the computer), In the Android studio environment, you should check that your phone is recognized. The simplest control is to display your phone model on the screen that opens by pressing `Shift + F10`.<br><br>
  ![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/telefon%20algilama.PNG)
  
  Now, all we have to do is click on the Terminal tab on the bottom left or press `Alt + F12`.
 On the opened terminal screen;
  * `adb shell`
  * `settings put global captive_portal_detection_enabled 0`<br><br>
  
   ![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/terminal%20detection%20enable%200.PNG)
   
  If everything goes well, you should type `settings get global captive_portal_detection_enabled` in this command and the terminal should also type `0 (zero)`.<br>
  If you see `0 (zero)`, you can now connect and use the car smoothly <br>
  
* **2nd METHOD**
   * Settings ==> Wireless ==> Pi_CAR ==> Advanced Options
   <br>
   **Password:** TRaspberry<br>
   **IP settings** = Statik<br>
   **Ip address** = 192.168.57.57<br>
   **Gateway** = 192.168.57.1<br>
   **Network prefix length** = 24<br>
   **DNS 1** = 8.8.8.8<br>
   **DNS 2** = 8.8.4.4<br>
   <br>
   Once you have entered the required information above, click Connect. And get ip address and connect. Then if you get a warning that you do not have internet access on your wireless connection, press yes again after you select the Ask again for this network option. <br><br><br>
   **VIDEO EXPRESSION**<br>
    
   [![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/youtube%20play2.png)](https://youtu.be/qp3TYz8y5Tc)
<br>
   And everything is okay. You can now use the application.

#### Raspberry Pi Connection Informations

Once you've downloaded your Android app, you will see the following welcome : Now all you need to do is check the tool. screen.<br>
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/Screenshot_20170124-151222.png)
<br>
Let's briefly explain the working principle and the introduction of the application.
#### APPLICATION DETAILS

##### 1. EXPLAINING OF THE VISUAL DESIGN AND PROGRAMMING LOGIC
**Our application rely on 3 basis. These are;**<br><br>
 I.Providing direction control of the vehicle and camera movement.(There are 3 different control methods as Joystick, Button and Vr (Camera movement).)<br>
 II. Transfer live video streaming from car to user.<br>
 III. Connection signal level indicator of vehicle.<br>
 
 * To that 3 basis;
* We will explain the vehicle with the side facing the android side in direction control.On the Android side, there are 3 different control interfaces for the user. These are directional control buttons, joystick and VR. **Now let's examine these 3 control interfaces**

## Button Control Interface<br>
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/IMG_20170123_013621_334.jpg)
<br><br>
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/Screenshot_description_en.png)
<br><br>

`Seek bar (Velocity setting)`, `Camera On / Off`,`Wi-Fi status indicator` and `Arrow keys` are available.<br><br> 

* **Seek bar(Velocity setting)**is created from `15` slice and velocity coefficient is `6.66`. So any move of the Seek bar, there will be changing `6.66` and its multiples. For instance, If Seek bar in fifth order, produced pwm = `5*6.66 = 33.3`. And it is rounded to 33.

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
 
## Joystick Control Interface
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/IMG_20170123_013536_641.jpg)<br><br>
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/joysick_control_en.png)

* There are 2 joystick control interfaces for controlling the car and the camera. From these interfaces, the directional control of the vehicle on the left, while the right side provides directional control of the camera on the vehicle. The point to note in the joystick control interface is the maximum speed setting. The maximum speed setting here specifies the maximum speed at which the vehicle can travel. The camera speed is fixed. The pwm range generated by raspberry pi is considered when determining the maximum speed setting.  <b> This range is 0-100. </b> <br>
 The maximum speed range you will set for the vehicle should be between <b>0-100</b>
<br><br>

## For further information or if you have any questions please do not hesitate to [contact me!](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/issues)

<br><br>

## VR Control Interface

![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/Screenshot_vr.png)
<br> <br>
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/Screenshot_20170122-205445.png)
<br>
* In the VR interface, you need to pay attention to the calibration of the instrument's sensors. In the application, two kinds of sensor calibration are done.
* **1. Calibration;** Automatically by the application, magnetometer and gyroscope data are filtered and a reference value is taken according to the geography of the earth.
* **2. Calibration;** The calibration we need to do manually. After bringing our head to the reference (point where we want), you need to click on the compass icon from the menu bar. This calibration refers to the origin (center point) of our head (according to Calibration 1). After this second calibration, the vehicle camera will move towards that point wherever you turn your head.

* **NOTE:** When VR mode is selected, a second device is required for motion control of the vehicle. Again, in the same way, Via a second android phone as you can control using other control interfaces, In our developed Microsoft application, you can check with the help of Fly Joystick. ![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/Retro-Games32x32.png) 
   <br><br>
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/vr_aciklama_EN.png)<br>   
<br><br>

## For further information or if you have any questions please do not hesitate to [contact me!](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/issues)





## ![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/Microsoft-windows-8-icon32x32.png)    WINDOWS: <br>   

### PURPOSE AND MISSIONS:
* Provide direction control of the car.
* Simple and easy visual interface for the user.

### WINDOWS "Pi_CAR" APPLICATION INSTALLATION AND CONFIGURATION SETTINGS:
* Pi_CAR has no camera support in windows application, Without a camera view, free use is offered for those who want to drive vehicle.
* **For the activation of the application you need to have your internet connection during the initial installation.** Appart from that, there is nothing  to pay attention to.
* The installation  of the application is extremely simple. All you have to do  is install the setup file.<br>

<p align="center">
 <a href="https://play.google.com/store/apps/details?id=com.stackcuriosity.tooght"><img src="https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/windows_pi_cart.png"/></a>
</p>
### APPLICATION USAGE AND TIPS. <br>
* Windows application; There is only Fly joystick  support at the moment to control the vehicle..<br><br>
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/IMG_20170123_013829_033.jpg)<br>   
* The point to note in the Windows control interfaces is the maximum speed setting. The maximum speed setting here indicates the maximum speed at which the vehicle can reach. The pwm range generated by raspberry pi is considered when determining the maximum speed setting.<b> This range is 0-100 </b>. The maximum speed range you will set for the vehicle shuould be between<b> 0-100.</b>
<br><br>
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/windows_aciklama.png)<br><br>
**NOTE:**
* The main purpose of this windows application, during use of the VR control interfaces on Android, it is possible to move the vehicle  as an alternative to the android application.



-------------------------------------------------------------------------------------
<br><br>
#<p align="center"> <b>BRIEF AND ABSTRACT INSTALLATION</b></p>
<br><br>
<p align="center"> <b>FOR DETAILED  INFORMATION AND INISTALLATION, PLEASE START AT THE TOP OF THE PAGE.!!</b>
<img src="https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images//images/raw.gif" alt="DETAYLI ANLATIM VE KURULUM" align="middle" />
</p>


## **STEP 1:**
* 1.If you want to manage Pi_CAR via Raspberry pi 2 or  the built-in Wi-Fi module on the Raspberry Pi 3.Download the operating system on [**this link**](https://drive.google.com/open?id=0B6yjwSAqPTgfcHRRLXYwMHZ6RWs)  and print to the SD card.
<br>


## **STEP 2**
* [Click!](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/ENGLISH/V3/select_Vehicle_en.md) on the sample vehicle selection and the appropriate pin connection of the vehicle. 

## **STEP 3**
* Download the Android control software from this  [**link**](https://play.google.com/store/apps/details?id=com.stackcuriosity.tooght) and upload to Android Phone. 
<br><br><br>
<p align="center">
 <a href="https://play.google.com/store/apps/details?id=com.stackcuriosity.tooght"><img src="https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images//images/Google.png"/></a>
</p>

## **ADIM 4** 
* Download and installation the windows control software from this [**link**](https://play.google.com/store/apps/details?id=com.stackcuriosity.tooght) 

<p align="center">
 <a href="https://play.google.com/store/apps/details?id=com.stackcuriosity.tooght"><img src="https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/windows_pi_cart.png"/></a>
</p>
<br>
**And the operation is complete. If you have correctly connected the Raspberry pi motor drivers, you can now start checking the vehicle.**

## For further information or if you have any questions please do not hesitate to [contact me!](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/issues)
<br><br>
### ICON OF OUR APPLICATION:

![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V1Images/images/raspi_car.png)


## TEST VIDEO:
[![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V1Images/images/testvd1.png)](https://youtu.be/qbkH2KFcKqw)
[![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/play_video2.png)](https://youtu.be/CT-hgXIPRIk)<br><br>
