/********************************************                  WiFi-RC-Controller-With-Camera                 **************************************************************/
/*                              ##############################            ARDUINO CODE   ENGLISH INFORMATION               ##########################                         */
/*
 * 
 * 
 * 
 * motor directions
 * yonVer(1,2,3,4,5);
 * 1: right motor to the forward
 * 2: right motor to the backward
 * 3: left motor to the backward
 * 4: left motor to the forward
 * 
 * We are taking LEFT and RIGHT motor PWMs and servo motor angle from phone by String (Exm: 200:200!888). Create an array with have three elements by colon ':' and exclamation '!' signs between numbers.
 * 
 *  The value after '!' is an servo motor's angle value which connect to the camera. In this work, we don't use any servo.
 * 
 * 
 * Motor Moving, PWM data and situations of the car
 * 
 * örn:
 * 
 * 
 *  0:0      //stop
 * 200:200     // move forward. (2 motors work with 200pwm)
 *  -200:-200   // move backward. (2 motors work with 200pwm)
 *  200:-200   // left motor turns 200 pwm to forward, right motor turns 200 pwm to backward (The car turns its around from left to right.)
 * -200:200   // left motor turns 200 pwm to backward, right motor turns 200 pwm to forward (The car turns its around from right to left.)
 * 200:100    // The car moves as turning to the right.
 * 
 * 
 * 
 *  9000 //upward servo
 *  27000 //downward servo
 *  0000 //right servo
 *  18000 //left servo
 * 
 * 
 * 
 *   servo1 =z axis (the servo that moving upward and downward)
 *   servo2 = x axis (the servo that moving left and right)
 *  
 *  
 *    ls /dev/tty* //raspberry usb list
 *    
 *    
 *    
 *       
 */


#include <Servo.h>
Servo servo1, servo2;
//sağ motor pinleri
const int SagL = 11;                 //  /*
const int SagR = 3;                  // *               ARDUİNO NANO PWM PINS THAT GO TO L298 MOTOR DRIVE
                                     // *                            (FOR MOTOR CONTROL)
//Sol motor pinleri                  // *                
const int SolL = 6;                  // *
const int SolR = 5;                  // */


String dizi[3];                             // We defined an array with 3 elements



void setup() {
  pinMode(SagL, OUTPUT);                  ///*
  pinMode(SagR, OUTPUT);                  //*       We set the arduino pins as PWM output 
  pinMode(SolL, OUTPUT);                  //*
  pinMode(SolR, OUTPUT);                  //*/



  Serial.begin(200000);                       // This is a USB communication speed between Arduino and Raspberry Pi.(Baud Rate)
  Serial.setTimeout(10);                        // Waiting time for data coming from serial communication. (Milliseconds.Default =1000ms)
}
void loop() {
  if (Serial.available()) {
    String gelenDeger = Serial.readString();                      // We defined a String for data coming from Serial
    //Serial.println(gelenDeger);
    int commaIndex = gelenDeger.indexOf(':');                     // We take the index number of the colon ':' sign (return int )
    int commaIndex2 = gelenDeger.indexOf("!");                    // Also we take the index number of the colon ':' sign (return int)

    if (commaIndex != (-1 ) && commaIndex2 != (-1)) {             // For prevent the errors, we check ':' and '!' values in the coming data.
      gelenDeger.trim();                                          // If the gap in the start or end of the data coming from Serial, we destroy them
     
      dizi[0] = gelenDeger.substring(0, commaIndex);                      //*/
      dizi[1] = gelenDeger.substring(commaIndex + 1, commaIndex2);        //*             
      dizi[2] = gelenDeger.substring(commaIndex2 + 1);                    //*     We split the data with '!' and ':'
      dizi[0].trim();                                                     //*     We destroy the gaps among assigned values
      dizi[1].trim();                                                     //*
      dizi[2].trim();                                                     //*/

      int X = (dizi[0].toInt());                                        //* First two values (motor PWM values) translated from String type to int type.
      int Y = (dizi[1].toInt());                                        //*
     
      
      
      yonVer(X, Y);                                                     // We assigned to "yonver" method the X and Y parameters.

    }


  }

}





void yonVer(int X, int Y)
{
  int a = 0, b = 0, c = 0, d = 0;
  if(X<0)
    b = X *-1;
  else if(X>0)
    a = X;

  if(Y<0)
    c = Y * -1;
  else if(Y > 0)
    d = Y;

  yonVer(a, b, c, d);
}

void yonVer(int a, int b, int c, int d) {

  analogWrite(SagL, a);
  analogWrite(SagR, b);

  analogWrite(SolR, c);
  analogWrite(SolL, d);
}
