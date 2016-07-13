# RASPBERRY PI- ARDUINO ANDROID-CONTROLLED RC-CAR ROVER WITH LIVE VIDEO STREAMING

## About this project?

* Direction control via Android
* Video streaming from RC-Car to mobile phone simultaneously
* Follow Me (Very Soon)

[![Screen Shot](images/yotubeT1.png)](https://youtu.be/J8r_bX_RNzU)


## Materials
* Arduino Nano
* Raspberry Pi
* Raspberry Pi Camera Module
* L298N Motor Drive
* DC MOTOR X  2 
* 12V Lipo Battery
* Car Frame (Body)


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
* Motor Moving, PWM data and situations of the car
* Example:
* 0:0 //stop
* 200:200 // move forward. (2 motors work with 200pwm)
* 200:-200 //move backward. (2 motors work with 200pwm)
* 200:-200 // left motor turns 200 pwm to forward, right motor turns 200 pwm to backward (The car turns its around from left to right.)
* 200:-200 // left motor turns 200 pwm to backward, right motor turns 200 pwm to forward (The car turns its around from right to left.)
* 200:100 // The car moves as turning to the right.<br><br>
 



[![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/images/youtbeT2.png)](https://youtu.be/D4ewbO-OGLY)

![Screen shot WiFi Maunt](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/images/wificontrol.png)
<br><br>
* Connections among Arduino, Raspberry pi,Raspberry pi camera module, L298N motor driver, Motors and Power Supply are set up as above picture.
* After connected Arduino pins and Raspberry pi as above picture, we can load our codes to Arduino. That do by this sequence:
* Detail information about Arduino codes is placed in that codes.
* Download `androidToRaspberry.ino` file and open this file with double click.
* For uploading that project file to Arduino, first you must select the Arduino model from `Tools => Board` menu.<br><br>


![Screen Shot RA1](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/images/ra1.png)
<br><br>
* Again from `Tools` menu, you must show which port plugged to Arduino board. `Tools => port`
* After realize all steps, now you can upload the codes to Arduino board. You can complete the uploading process by pressing `Upload` button from left-up corner of the program.<br><br><br>
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/images/ra2.png)
<br><br>

## RASPBERRY PI:
### PURPOSE AND MISSIONS:

* Taking video stream with Raspberry Pi camera module and trasfer that stream to phone via Raspberry pi.
* Connection between Arduino and Android phone.

### RASPBERRY PI SETUP:

We need some additional packages for can work our application. **These are;**<br>

**GSTREAMER1.0 :**<br>
After connect with SSH, we must type that in order:<br>


* 1.	Write `sudo nano /etc/apt/sources.list`
and press Enter. From coming screen;<br><br>
![Screen Shot](images/r1.png)<br><br>

* 2.	 Write `deb http://vontaene.de/raspbian-updates/ . main`
command and exit the page with **CTRL + O  ==>  Y**  <br><br>
![Screen Shot](images/r2.png)<br><br>

* 3. Write 	`sudo apt-get update` and get latest updates. <br><br>
![Screen Shot](images/r3.png)<br><br>

Then by turns, apply that steps:

* 4.	`sudo apt-get dist-upgrade`

* 5.	`sudo reboot`

* 6.	`sudo apt-get install gstreamer-1.0`<br><br>![Screen Shot](images/r4.png)<br><br>

* 7.	`sudo apt-get install gstreamer1.0-tools`<br>

And after this steps, we installed gstreamer package.<br><br>



**SETUP MAIN FILE:**

Now we install the main file of the application;

* 1. We are downloading our GitHub file in Raspberry pi terminal screen.<br>`git clone https://github.com/zafersn/Wi-Fi-Gstreamer-Server.git`
      
* 2.	Also with `ls` command with control that file. The file which we downloaded is shown as a `Wi-Fi-Gstreamer-Server` name.

* 3.	Write `cd Wi-Fi-Gstreamer-Server` and enter in the file. You can see with `ls` command a `robotcontrolV1.pyc` named python application.

* 4. We need to move this file with `sudo cp robotcontrolV1.pyc /home/pi` command to our `/home/pi` directory. If you can't do this, application is not working correctly.<br><br><br>![Screen Shot](images/r5.png)<br><br>

* 5.  In case of skip that steps successfully, we give our first start on the Raspberry Pi manually. Because, this is useful for us to see working this application.

* 6. Execute the application manually: execute the program with `sudo python robotcontrolV1.pyc` command in main terminal. If you are setting up until this step successfully, you must see `Client Baglantisi Bekleniyor...` print.

* 7. Last, you try to conncect from Android phone to Raspberry Pi via our application.

* 8. If we are execute our Python code (`robotcontrolV1.pyc`) in Raspberry Pi manually, our phone's IP and port informations will appear in the screen when we connect from Android.

 













## ANDROID:

### PURPOSE AND MISSIONS:
* Maintaining control of RC-Car that made from Android and Raspberry Pi.
* Simple and pure design for user.
* Taking video stream via Raspberry Pi and show this to user.

### INSTALL ANDROID APPLICATION:
*  There are two application for car control; that are pro and demo versions of the application. There is no difference between pro and demo version of the application in point of using features. Only in demo version using count of the application is restricted. This using count is 30 and this can be increased and decreased by administator. (Note: When calculaing of the using count, there won't be used entering to application or exiting from application, there will be used in connecting and controlling from Android to RC-Car successfully. For increasing using count in that case, system must work as a whole. Peace of mind there can be downloaded the application and there can be used the system as a freeware from your side.)
- When above-mentioned case is considered, installing of the application is very simple. Only after enter the **ANDROID GOOGLE PLAY** market, you can type in searching box `com.stackcuriosity.tooght` or application name `Wifi RC Controoller with Camera` for directly access to application.

### USING THE APPLICATION AND HINTS
#### Raspberry Pi Connection Informations
* When the application is opened as a first, user see login screen as the following picture. You need to do in this screen, only entering the Wi-Fi informations which connected of Raspberry pi.<br><br>![Screen Shot](images/device-2016-06-30-193829.png)<br><br>

* Example entered informations:<br><br><br>![Screen Shot](images/device-2016-06-30-200150.png)<br><br>
* When you enter this infos succesfully, you will see the following welcome screen.<br><br>![Screen Shot](images/device-2016-06-30-195734.png)<br><br>
*  If you don't connect to Raspberry pi for any situation and if you see the `The connection fails.Please try again.` screen, please check the Raspberry Pi connections and your connection infos. Because, the reason of the this error is your phone can't connect to `robotcontrolV1.pyc` file that your creating and executing.<br><br>![Screen Shot](images/device-2016-07-08-001102.png)<br><br>
* For solve that problem, you consider the `SETUP MAIN FILE` section again and check the installation.

#### APPLICATION DETAILS

##### 1. EXPLAINING OF THE VISUAL DESIGN AND PROGRAMMING LOGIC
* Our application rely on 3 basis. These are;
* 1. Provide direction control of the car.
* 2. Transfer live video streaming from car to user.
* 3. Follow Me (Vey Soon). (Following the car its owner.)
* To that 3 basis;
* 1. Main details using direction control of the car was told in `Arduino` section. If we explain to the Android side, there will be available `Seek bar (Velocity setting)` and `Arrow keys`.<br><br> ![Screen Shot](images/kontrol_ekrani_anlatim.png)<br><br>
*  **Seek bar(Velocity setting)**is created from 15 slice and velocity coefficient is 17. So any move of the Seek bar, there will be changing 17 and its multiples. For instance, If Seek bar in fifth order, produced pwm = 5*17 = 85.
* **Arrow keys** provide seperating directions of data which take from Seek bar(Velocity setting). For moving direction of the car, `+` or `-` sign come to head of the PWM value. For example:

* 200:200 // move forward. (2 motors work with 200pwm)
* 200:-200 //move backward. (2 motors work with 200pwm)
* 200:-200 // left motor turns 200 pwm to forward, right motor turns 200 pwm to backward (The car turns its around from left to right.)
* 200:-200 // left motor turns 200 pwm to backward, right motor turns 200 pwm to forward (The car turns its around from right to left.)
* 200:100 // The car moves as turning to the right.<br><br> 

##### 2.SENSITIVITY IN TURNING LEFT AND RIGHT
* When our car moving to right cross and left cross, motors' PWM value which will be turning side decreases, and so this provides slower motor rotating. So, the car can achieve the intended turnings. **This rotating sensitivity setting let to user.**
* The formula for calculating cross turnings: **PWM VALUE - ((PWM VALUE) / PWM RATE)**
* In default, PWM RATE is `2`.
* You can reach the PWM RATE setting from right-top button in the screen and from there to `Settings` menu.<br><br>![Screen Shot](images/device-2016-07-07-230804.png)<br><br>![Screen Shot](images/device-2016-07-07-230848.png)<br><br>
*  PWM interval which can be entered is a value as a **minimum and maximimum between 1-4 interval in integer and double type**.
 


### ICON OF OUR APPLICATION:

![Screen Shot](images/raspi_car.png)




## TEST VİDEO:
[![Screen Shot](images/testvd1.png)](https://youtu.be/qbkH2KFcKqw)
