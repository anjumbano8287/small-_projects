import os 
import datetime
import time

try:
    year,month,date =map( int,input("enter the year,monthand date  yy/mm/dd").split("/"))
    hours,minutes,seconds =map(int,input("enter the hour ,minutes and seconds").split(":"))
    schedule=datetime.datetime(year,month,date,hours,minutes,seconds)
    
except ValueError as e:
    print("invalid date or time")     
    exit() 
print(schedule)
while True:
    now =datetime.datetime.now()
    if now>=schedule:
        try:
            os.startfile(r"C:\Users\HP\Downloads\twirling-intime-lenovo-k8-note-alarm-tone-41440.mp3")
        except ValueError as e:
            print("file not found") 
        break
time.sleep(1)           


