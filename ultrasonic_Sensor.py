
#Libraries
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 21
GPIO_ECHO = 20
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


 # Pins for Motor Driver Inputs 
Motor1A = 6
Motor1B = 13
Motor2A = 19
Motor2B = 26

GPIO.setup(Motor1A,GPIO.OUT)  # All pins as Outputs
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)  # All pins as Outputs
GPIO.setup(Motor2B,GPIO.OUT)

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

def mail():
    import smtplib
    from email.message import EmailMessage
    import imghdr

    Sender_Email = "roboproject007@gmail.com"
    Reciever_Email = "kaustubhshivanekar@gmail.com"
    Password ='fmbh jsna yiqg pvhl'
    newMessage = EmailMessage()    #creating an object of EmailMessage class
    newMessage['Subject'] = "Test Email for Object Detection" #Defining email subject
    newMessage['From'] = Sender_Email  #Defining sender email
    newMessage['To'] = Reciever_Email  #Defining reciever email


    import requests 
    api_address = "http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
            
    import json
    location_req_url='http://api.ipstack.com/2401:4900:5039:4b15:7e45:5534:75:3d5?access_key=f5ebf0974241e6218f17ad8737d77286'
    r = requests.get(location_req_url)
    location_obj = json.loads(r.text)
            
    lat = location_obj['latitude']
    lon = location_obj['longitude']
    latitude = lat
    longitude = lon
    print(str(latitude))
    print(str(longitude))


    newMessage.set_content('Hi,Detect Object.... \n Here I attached Object location: \n Latitude is:'+str(latitude)+'\n Langitude is:'+str(longitude)) #Defining email body
   
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        
        smtp.login(Sender_Email, Password)              
        smtp.send_message(newMessage)

 
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            if (dist < 30):
                print("Object detected")
                GPIO.output(Motor1A,GPIO.LOW)
                GPIO.output(Motor1B,GPIO.LOW)
                GPIO.output(Motor2A,GPIO.LOW)
                GPIO.output(Motor2B,GPIO.LOW)
                mail()
                
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
