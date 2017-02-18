
# Vehicle Type 1: Single-motor, Servo steering <br><br>



![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/IMG_20170118_191443_488.jpg)<br><br>
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/IMG_20170109_181102.jpg)<br>
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/IMG_20161226_171613.jpg)<br>
* This vehicle used one motor for back and forth movement and one motor driver for driving this motor.
 * The BTS7960 was preferred here as the engine driver. L298N / L293 etc.  Motor drives can be used.
* A servo motor was used for steering movements. <br>
* 2 servo motors used for camera movements.

### LIST OF MATERIALS
Product name| Piece
----| ---- 
Raspberry Pi| 1
Raspberry Pi Camera Module| 1
Wi-Fi Adaptör| 1 (Optional for Pi 3)
L298N,BTS7960,L293 Motor Drive| 1 
DC MOTOR|  1  
SERVO MOTOR| 3
12V Lipo Battery| 1
Jumper Cable | ~
Vehicle Chassis| 1
5V Power Supply or Power Bank  [**(LM2596-ADJ)**](http://www.robotistan.com/mini-ayarlanabilir-3a-voltaj-regulator-karti-lm2596-adj) or [**(2A Mini)**]( http://www.robotistan.com/2a-mini-ayarlanabilir-voltaj-dusurucu-regulator-karti)|1
<br>

## THE CONNECTION DIAGRAM IS AS FOLLOWS <br><br>

### RASPBERRY PI PIN CONNECTIONS
PIN NAME| GPIO NUMBERS (BCM)
----| ---- 
SERVO MOTOR FOR STEERING CONTROL| GPIO 16
SERVO MOTOR FOR CAMERA VERTICAL AXIS MOVEMENT| GPIO 15
SERVO MOTOR FOR CAMERA HORIZONTAL AXIS MOVEMENT| GPIO 14
MOTOR DRIVE FOR RIGHT PWM | GPIO 13
MOTOR DRIVE FOR LEFT PWM| GPIO 19
MOTOR DRIVE FOR RIGHT ENABLE PIN| GPIO 23
MOTOR DRIVE FOR LEFT ENABLE PIN| GPIO 24
5V POWER VCC  | 5V INPUT
5V POWER GND | GND INPUT
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/RasPiO-portsplus2-on-pi_1500.jpg)<br><br>

* **IMPORTANT NOTE 1** Here's what you need to look out for: If you misplug the motor drivers and the camcorder's pins, the car or camera will only have the wrong movements. But if you plug the 5V power supply into the wrong or wrong pins, irreversible damage can occur in the raspberry. Ahududaki iğnelerin güç girişine alternatif olarak, mikro usb girişinizi ahududu pi'de de kullanabilirsiniz(Power bank etc. , Other alternative.)

* **IMPORTANT NOTE 2:** You should not feed your raspberry and servo motors directly from the same power supply. Kısacası, LV2596 ile 5V üretiyorsanız, Ahududanı ve Servo motorları doğrudan çalıştırmamalısınız.

![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/pin_baglanti%20servo_en.PNG)
<br><br>
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/pin_baglanti_servo_schmatic_en.PNG)
<br><br>


## Please  [ask!](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/issues) what you do not understand.



<br><br>

# Vehicle Type 2: Tank Type Vehicle <br><br>

* There are 2 direction control motors, right and left engine. The operation is shaped like a tank.
* As can be seen from the pictures below, the rotation speed difference between the right and left motors is used for right and left turns.
<br>


<p align="center" width="640" height="480" > <b>6 X 6 VEHICLE !!</b>
<a href="https://www.youtube.com/watch?v=06LrVjRDfS8"><img src="https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/giphy.gif" alt="DETAYLI ANLATIM VE KURULUM" align="middle" />
</a></p>


<br>
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/IMG_20160201_001625.jpg)<br><br>


![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/IMG_20151122_142027.jpg)
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/IMG_20151122_141900.jpg)

### LIST OF MATERIALS
Product Name| Piece
----| ---- 
Raspberry Pi| 1
Raspberry Pi Camera Module| 1
Wi-Fi Adaptor| 1 (Pi 3 için isteğe bağlı)
L298N,BTS7960,L293 Motor Drive| 1 or 2 
DC MOTOR|  2 or 4
SERVO MOTOR| 2
12V Lipo Battery| 1
Jumper Cable | ~
Vehicle Chassis | 1
5V Power Supply  [**(LM2596-ADJ)**](http://www.robotistan.com/mini-ayarlanabilir-3a-voltaj-regulator-karti-lm2596-adj) or [**(2A Mini)**]( http://www.robotistan.com/2a-mini-ayarlanabilir-voltaj-dusurucu-regulator-karti)|1
<br>

* This vehicle used 6  (3/3) motors in total for moving back and forth / right and left and two motor drives for driving this motor.
 * The BTS7960 was preferred here as the engine driver. L298N / L293 etc.  Motor drives can be used.
* The difference in rotation speeds of the right and left side motors was used for steering movements. <br>
* Two servo motors were used for camera movements.


## THE CONNECTION DIAGRAM IS AS FOLLOWS <br><br>

### RASPBERRY PI PIN CONNECTIONS
PIN NAME| GPIO NUMBERS (BCM)
----| ---- 
SERVO MOTOR FOR CAMERA VERTICAL AXIS MOVEMENT| GPIO 15
SERVO MOTOR FOR CAMERA HORIZONTAL AXIS MOVEMENT| GPIO 14
RIGHT MOTOR DRIVE FOR RIGHT PWM | GPIO 13
RIGHT MOTOR DRIVE FOR LEFT PWM| GPIO 19
LEFT MOTOR DRIVE FOR RIGHT PWM | GPIO 18
LEFT MOTOR DRIVE FOR LEFT PWM| GPIO 12
MOTOR DRIVE FOR RIGHT ENABLE PIN| GPIO 23
MOTOR DRIVE FOR LEFT ENABLE PIN| GPIO 24
MOTOR DRIVE FOR RIGHT ENABLE PIN| GPIO 20
MOTOR DRIVE FOR LEFT ENABLE PIN| GPIO 21
5V POWER VCC  | 5V INPUT
5V POWER GND | GND INPUT
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/pin_baglanti_tank_en.PNG)<br><br>
<br><br>
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/pin_baglanti_tank_sematik_en.PNG)
<br><br>
* **IMPORTANT NOTE 1** Here's what you need to look out for: If you misplug the motor drivers and the camcorder's pins, the car or camera will only have the wrong movements. But if you plug the 5V power supply into the wrong or wrong pins, irreversible damage can occur in the raspberry. Ahududaki iğnelerin güç girişine alternatif olarak, mikro usb girişinizi ahududu pi'de de kullanabilirsiniz(Power bank etc. , Other alternative.)

* **IMPORTANT NOTE 2:** You should not feed your raspberry and servo motors directly from the same power supply. Kısacası, LV2596 ile 5V üretiyorsanız, Ahududanı ve Servo motorları doğrudan çalıştırmamalısınız.

<br><br>
## Please  [ask!](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/issues) what you do not understand.
