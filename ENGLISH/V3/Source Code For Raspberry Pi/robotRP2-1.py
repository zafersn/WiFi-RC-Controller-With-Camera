try:
  import RPi.GPIO as GPIO
  import time
  from socket import *
  import signal
  from subprocess import call
  import time
  import os
  import subprocess
#  from threading import Thread
  import threading
except RuntimeError:
  print("Error importing RPi.GPIO! This must be run as root using sudo")
import sys, tty, termios
print 'Client Connection Waiting...'

#----------------------------------------------------------------------------
#GPIO.cleanup()
# GPIO settings and definitions
p1Sol=13  #we identified the pins
p1Sag=19
p2Sol=18
p2Sag=12


enSag1=23
enSol1=24
enSag2=20
enSol2=21
servoPWM=16

servoCamPWM_V=15
servoCamPWM_H=14

try:
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(p1Sol,GPIO.OUT)
	GPIO.setup(p1Sag,GPIO.OUT)
	GPIO.setup(p2Sol,GPIO.OUT)
	GPIO.setup(p2Sag,GPIO.OUT)
	GPIO.setup(enSol1,GPIO.OUT)
	GPIO.setup(enSag1,GPIO.OUT)
	GPIO.setup(enSol2,GPIO.OUT)
	GPIO.setup(enSag2,GPIO.OUT)
	GPIO.setup(servoPWM,GPIO.OUT)
	GPIO.setup(servoCamPWM_V,GPIO.OUT)
	GPIO.setup(servoCamPWM_H,GPIO.OUT)

	p1SolPWM=GPIO.PWM(p1Sol,1000)
	p1SagPWM=GPIO.PWM(p1Sag,1000)
	p2SolPWM=GPIO.PWM(p2Sol,1000)
	p2SagPWM=GPIO.PWM(p2Sag,1000)
#for front wheel freezing servo motor (vehicle type 1)
	pServoPWM=GPIO.PWM(servoPWM,100)
# For the camera's servo motor
	pServoCAM_PWM_V=GPIO.PWM(servoCamPWM_V,100)
	pServoCAM_PWM_H=GPIO.PWM(servoCamPWM_H,100)
	
except RuntimeWarning:
        GPIO.cleanup()
p1SolPWM.start(0)
p1SagPWM.start(0)
p2SolPWM.start(0)
p2SagPWM.start(0)

pServoPWM.start(5)
pServoCAM_PWM_V.start(5)
pServoCAM_PWM_H.start(5)

GPIO.output(p1Sag,GPIO.LOW)
GPIO.output(p1Sol,GPIO.LOW)
GPIO.output(p2Sag,GPIO.LOW)
GPIO.output(p2Sol,GPIO.LOW)

GPIO.output(enSol1,GPIO.HIGH)
GPIO.output(enSag1,GPIO.HIGH)
GPIO.output(enSol2,GPIO.HIGH)
GPIO.output(enSag2,GPIO.HIGH)
#-----------------------------------------------------------------------------

sock = socket(AF_INET, SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
print gethostname()
UDP_IP = "192.168.42.13"
UDP_PORT = 5000
sock.bind(('', 5000))
def catch_ctrl_c(sig,frame):
	print "No gonna quit !!"
signal.signal(signal.SIGINT,catch_ctrl_c)
signal.signal(signal.SIGINT,signal.SIG_IGN)
signal.signal(signal.SIGTSTP,signal.SIG_IGN)
def readDataWifi():
 a=0
 while True:
#The client receives the received data and assigns it to the data variable.
   try:

	 data,addr=sock.recvfrom(1024)
	 print "ip: ",addr
         print "Gelen Mesaj:",data.strip()# , a
	 print len(data)
	 if(data.strip()=="9BBB"):
		print "! udpsink " + "host="+str(addr[0])+" port="+str(addr[1])+" &"
#		return_code = subprocess.call("raspivid -rot 180 -t 999999 -h 320 -w 640 -fps 10 -b 2000000 -o - | gst-launch-1.0 -v fdsrc fd=0 ! h264parse ! rtph264pay ! udpsink host=192.168.57.57 port=8554 &", shell=True)
		return_code = subprocess.call("raspivid -rot 180 -t 999999 -h 320 -w 640 -fps 10 -b 2000000 -o - | gst-launch-1.0 -v fdsrc fd=0 ! h264parse ! rtph264pay ! udpsink " + "host="+str(addr[0])+" port=8554"+" &", shell=True)
		print "returncode 1: ",return_code
	 elif(data.strip()=="10"):
		return_code = subprocess.call("sudo killall raspivid", shell=True)
		print "returncode 2: ",return_code
	 if ((data.strip()=="1.0711453")):
		print "ciktim"
		pSol1PWM.stop()
		pSag1PWM.stop()
		pSol2PWM.stop()
                pSag2PWM.stop()
		pServoPWM.stop()
		pServoCAM_PWM_V.stop()
	        pServoCAM_PWM_H.stop()		
		GPIO.cleanup()
		print "returncode 3: ",return_code
		return_code = subprocess.call("sudo killall raspivid", shell=True)
		sys.exit(0)
	 elif (data is not None) and not (data.strip() == "9BBB") and not (data.strip() == "10"):
		dataSol=(data.split(":",1)[0])
		dataSag=(data.split(":",1)[1].split("!")[0])
		if(dataSol=="Q"):
			dataVrDikeyEksen=(data.split(":",1)[1].split("!")[1])
			print dataVrDikeyEksen
		print (dataSol)
		print dataSag
		if (len((dataSol))==1):
			if(dataSol=="Q"):
				print "Q"
				servoCamVRcontrol(int(dataSag),int(dataVrDikeyEksen))	
			elif(not dataSol=="Q"):
				print "not Q"
				servoCameraKontrolJoystick(dataSol,dataSag)
			print '1111111111111111111'
		if(not (len((dataSol))==1)):
			print "22222222222222222222"
#			speedX = lambda sayi, maks, mini: ((sayi/float(maks-mini)))*100
#			speedZ = lambda sayi, maks, mini: ((sayi/float(maks-mini)))*100
#			print str(speedZ(int(float(dataSol)), 255, 0))
#			print str(speedX(int(float(dataSag)), 255, 0))
			yonKontrol(int(float(dataSol)),int(float(dataSag)))


		#pSolPWM.ChangeDutyCycle(dataSol)
		#GPIO.output(pSag,GPIO.LOW)
		#pSagPWM.ChangeDutyCycle(0)
		#pSolPWM.ChangeDutyCycle(dataSol)
		#pSagPWM.ChangeDutyCycle(50)					 	
	 else:
		print "gelen deger bilinmiyor",data
   except RuntimeError:
        print "hata var..."
	p1SolPWM.stop()
	p1SagPWM.stop()
	p2SolPWM.stop()
        p2SagPWM.stop()
	pServoCAM_PWM_V.stop()
	pServoCAM_PWM_H.stop()	
	GPIO.cleanup()

def servoCamVRcontrol(X,Y):
	servoUpdate_V(120+int(Y))
        servoUpdate_H(120-int(X))

def servoCameraKontrolJoystick(X,Y):
	print X
	print Y
	if(X=="z"):
		servoUpdate_V(120-int(Y))
	elif(X=="x"):
		servoUpdate_V(120-int(Y))
		servoUpdate_H(120-int(Y))
	elif(X=="c"):
		servoUpdate_V(120-int(Y))
		servoUpdate_H(120+int(Y))
	elif(X=="v"):
		servoUpdate_V(120+int(Y))
	elif(X=="b"):
		servoUpdate_V(120+int(Y))
		servoUpdate_H(120-int(Y))
	elif(X=="n"):
		servoUpdate_V(120+int(Y))
		servoUpdate_H(120+int(Y))
	elif(X=="m"):
		servoUpdate_H(120+int(Y))
	elif(X=="a"):
		servoUpdate_H(120-int(Y))
	elif(X=="s"):
		servoUpdate_V(120)
		servoUpdate_H(120)

def yonKontrol(X,Y):
	a=0
	b=0
	c=0 
	d=0
	if(X<0):
		b= X* (-1)
	elif (X>0):
		a= X
	if(Y<0):
		c= Y* (-1)	
	elif(Y>0):
		d= Y

	hareketKontrol(a,b,c,d)
def hareketKontrol(a,b,c,d):
# If the servo value is less than 100 , the vehicle turns to the right, and if the value is greater than 100 , it turns to the left.
	print 'a',a
	print 'b',b
	print 'c',c
	print 'd',d
	if(a>b): # go forward
		if(d>c and a==d): # just go forward
			p1SolPWM.ChangeDutyCycle(a) #d=10
                        p1SagPWM.ChangeDutyCycle(b) #c=0

			p2SolPWM.ChangeDutyCycle(c) #d=10
			p2SagPWM.ChangeDutyCycle(d) #c=0
			servoUpdate(120)
		elif(d>c and a>d) : #go forward to the left
			p1SolPWM.ChangeDutyCycle(a) #d=10
                        p1SagPWM.ChangeDutyCycle(b) #c=0

			p2SolPWM.ChangeDutyCycle(c) #a=10
			p2SagPWM.ChangeDutyCycle(d) #b=0
			servoUpdate(150)
		elif(d<c and a==c):# only for the left turn of the servos and not forwards and backwards
			p1SolPWM.ChangeDutyCycle(a) #d=10
                        p1SagPWM.ChangeDutyCycle(b) #c=0

			p2SolPWM.ChangeDutyCycle(c) #b=0
                        p2SagPWM.ChangeDutyCycle(d) #b=0
                        servoUpdate(150)
		else: # ileri git saga don
			p1SolPWM.ChangeDutyCycle(a) #d=10
                        p1SagPWM.ChangeDutyCycle(b) #c=0

			p2SolPWM.ChangeDutyCycle(c) #d=10
			p2SagPWM.ChangeDutyCycle(d) #c=0
			servoUpdate(80)
	elif(a<b):
		if(d<c and b==c):# just go back
			p1SolPWM.ChangeDutyCycle(a) #d=10
                        p1SagPWM.ChangeDutyCycle(b) #c=0

			p2SolPWM.ChangeDutyCycle(c) #a=0
			p2SagPWM.ChangeDutyCycle(d) #b=10 
			servoUpdate(120)
		elif(d<c and  b>c):# Go back, turn left.
			p1SolPWM.ChangeDutyCycle(a) #d=10
                        p1SagPWM.ChangeDutyCycle(b) #c=0

			p2SolPWM.ChangeDutyCycle(c)#a=0
			p2SagPWM.ChangeDutyCycle(d)#b=10
			servoUpdate(150)#servo left
		elif(d>c and b==d):#only for the servo to turn right.
			p1SolPWM.ChangeDutyCycle(a) #d=10
                        p1SagPWM.ChangeDutyCycle(b) #c=0

			p2SolPWM.ChangeDutyCycle(c)#a=0
                        p2SagPWM.ChangeDutyCycle(d)#a=0
                        servoUpdate(80)#servo right
		else:  # go back and turn right
			p1SolPWM.ChangeDutyCycle(a) #d=10
                        p1SagPWM.ChangeDutyCycle(b) #c=0

			p2SolPWM.ChangeDutyCycle(c)#a=0
			p2SagPWM.ChangeDutyCycle(d)#c=10 
			servoUpdate(80)#servo right
	else:		
			p1SolPWM.ChangeDutyCycle(0) #d=10
                        p1SagPWM.ChangeDutyCycle(0) #c=0
	
			p2SolPWM.ChangeDutyCycle(0)
			p2SagPWM.ChangeDutyCycle(0)
			servoUpdate(120)
		
def servoUpdate(angle):
	duty=float(angle) / 10.0 + 2.5
	if(duty<0):
                duty=0
        elif(duty>100):
                duty=100
	pServoPWM.ChangeDutyCycle(duty)

def servoUpdate_H(angle):
	print "=========================="
	print angle," :H"
	duty=float(angle) / 10.0 + 2.5
	if(duty<0):
		duty=0
	elif(duty>100):
		duty=100
	pServoCAM_PWM_H.ChangeDutyCycle(duty)
def servoUpdate_V(angle):
	print "=========================="
	print angle," :V"
	duty=float(angle) / 10.0 + 2.5
	if(duty<0):
                duty=0
        elif(duty>100):
                duty=100
	pServoCAM_PWM_V.ChangeDutyCycle(duty)

		
def sendData(data):
	sock.sendto(data,(UDP_IP, UDP_PORT))
def sendPacket(data,sock,data_size):
    packets = ["%s"%data[i:i+data_size] for i in range(0,len(data),data_size)]
    packets[-1] = packets[-1] + "\x00"*(len(data)%data_size)
    for p in packets:
        sock.sendto(p,(UDP_IP, UDP_PORT))

if __name__ == "__main__":
	lock = threading.Lock()
	GPIO.setwarnings(False)
	
	servoUpdate(100)
	servoUpdate_V(100)
	servoUpdate_H(100)
	

	readSocket = threading.Thread(target=readDataWifi, name='LockHolder')
#        readSocket.setDaemon(True)
        readSocket.start()
#	x=raw_input("please input q:")
#	if (x=="q"):
#		p1SolPWM.stop()
#		p1SagPWM.stop()
#		p2SolPWM.stop()
#	        p2SagPWM.stop()
#		pServoPWM.stop()
#		pServoCAM_PWM_V.stop()
#	        pServoCAM_PWM_H.stop()
#		GPIO.cleanup()
#		return_code = subprocess.call("sudo killall raspivid", shell=True)
#		sys.exit(0)
#	sendData("selamlar")
