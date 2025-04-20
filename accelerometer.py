#!/usr/bin/python

import time


import requests
import json
import Adafruit_ADS1x15
import smtplib
import requests
import json
from email.message import EmailMessage

location_req_url='http://api.ipstack.com/103.51.95.183?access_key=fcdaeccb61637a12fdf64626569efab0'
r = requests.get(location_req_url)
location_obj = json.loads(r.text)

lat = location_obj['latitude']
lon = location_obj['longitude']
city = "%s, %s, \n\r %s, %s" % (lat,lon,location_obj['city'], location_obj['region_code'])

Sender_Email = "roboproject007@gmail.com"
Reciever_Email = "kaustubhshivanekar@gmail.com"
Password ='fmbh jsna yiqg pvhl'

# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()
VALMAX = 15000
GAIN = 1
adcValue = 0;
offsetVoltage = 100;



def mapp( x, in_min, in_max, out_min, out_max) :
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;

def sensor_position ():
	pos = 0
	x = adc.read_adc(1, gain=GAIN)
	y = adc.read_adc(2, gain=GAIN)
	z = adc.read_adc(3, gain=GAIN)

	Xval = mapp (x,0,VALMAX,0,255)
	Yval = mapp (y,0,VALMAX,0,255)
	Zval = mapp (z,0,VALMAX,0,255)
	print ("X:"+str (Xval))
	print ("Y:"+str (Yval))
	print ("Z:"+str (Zval))
	time.sleep(2)
	if (Xval > 235 or Xval < 210) :
		pos = 1	
		return pos	
	if (Yval > 230 or Yval < 205) :
		pos = 1
		return pos
	else:
		pos = 0
		return pos
	
	

def mail(val) :
	newMessage = EmailMessage()    #creating an object of EmailMessage class
	newMessage['Subject'] = " " #Defining email subject
	newMessage['From'] = Sender_Email  #Defining sender email
	newMessage['To'] = Reciever_Email  #Defining reciever email
	if val == 1:
		newMessage.set_content('Advertising board tilted \r\nLocation ' + city) #Defining email body

	if val == 2:
		newMessage.set_content('Advertising board pole rusted \r\nLocation ' + city) #Defining email body
	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
		smtp.login(Sender_Email, Password)              
		smtp.send_message(newMessage)
def image():
    import cv2
    import time

    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)

    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
   
    else:
        rval = False

    while rval:
        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        cv2.imwrite('abc.jpg',frame)
        time.sleep(3)
        rval = False
        vc.release()
        cv2.destroyWindow("preview")
        break
def mail():
    from subprocess import call
    call(["python3", "mail.py"])
    

	

# Main loop.
while True:
	pos = sensor_position()
	
	if pos == 1 :
		print("Animal Falled")
		image()
		mail()
		
	else :
		print("Normal Condition")	
		
	time.sleep(1)


