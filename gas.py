import RPi.GPIO as GPIO
import time
import requests 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  # This command is to Disable Warning....!!!!

MQ_3 = 16
buzzer = 12
GPIO.setup(16, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)

def mail():
    import smtplib
    from email.message import EmailMessage
    import imghdr

    Sender_Email = "roboproject007@gmail.com"
    Reciever_Email = "kaustubhshivanekar@gmail.com"
    Password ='fmbh jsna yiqg pvhl'
    newMessage = EmailMessage()    #creating an object of EmailMessage class
    newMessage['Subject'] = "Test Email for Gas Detection" #Defining email subject
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


    newMessage.set_content('Hi,Detect Gas/Smoke.... \n Here I attached Object location: \n Latitude is:'+str(latitude)+'\n Langitude is:'+str(longitude)) #Defining email body
   
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        
        smtp.login(Sender_Email, Password)              
        smtp.send_message(newMessage)

    
'''################Location#################################################
import json
location_req_url='http://api.ipstack.com/103.51.95.183?access_key=fcdaeccb61637a12fdf64626569efab0'
r = requests.get(location_req_url)
location_obj = json.loads(r.text)
        
lat = location_obj['latitude']
lon = location_obj['longitude']
latitude = lat
longitude = lon
print(str(latitude))
print(str(longitude))
msg ="Smoke detected...Here I attached object:Latitude is:"+str(latitude)+"Langitude is:"+str(longitude)

###################################SMS###################################################
def sms_send():
    url="https://www.fast2sms.com/dev/bulkV2"
    params={
  
        "authorization":"NWc95zezpyn1Hah1cPF9ZKlV7d7ll9civgNwGrXQ1wb6sDk5jAnuOeCCQNl",
        "sender_id":"SMSINI",
        "message":"Smoke  detected...Here I attached object:Latitude is:"+str(latitude)+"Langitude is:"+str(longitude),
        "language":"english",
        "route":"q",
        "numbers":"7887369235"
    }
    rs=requests.get(url,params=params)

    
################################################################################'''#############

    
while True:
    j1=GPIO.input(MQ_3)
    print(j1)
    if j1==0 :
        print('Smoke Detected!')
        time.sleep(1)
        GPIO.output(buzzer, True)
        time.sleep(1)
        GPIO.output(buzzer, False)
        mail()
        '''sms_send() 
        import requests 
        #api_address = "http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
                        
        import json
        location_req_url='http://api.ipstack.com/2401:4900:5039:4b15:7e45:5534:75:3d5?access_key=f5ebf0974241e6218f17ad8737d77286'
        r = requests.get(location_req_url)
        location_obj = json.loads(r.text)
                        
        lat = location_obj['latitude']
        lon = location_obj['longitude']
        latitude = lat
        longitude = lon
        print(str(latitude))
        print(str(longitude))'''
       
    else :
        print ('Smoke Not Detected!')
        time.sleep(1)
