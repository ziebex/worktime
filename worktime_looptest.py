from datetime import datetime, timedelta
import sys
import re


def format_time(raw_time):
	colon = arrive_time.split(":")
	arrive_hour = int(colon[0])
	arrive_min = int(colon[1])
	start_time = datetime.now().replace(hour=arrive_hour,minute=arrive_min,second=0,microsecond=0)
	return(start_time)


def calculating_time(start):
	end_work = (start +  timedelta(hours=8)) - datetime.now()
	return(format(end_work))


while True: 
    arrive_time = input('Your time: ')
    if re.match('^[0-24]:[0-59]$', arrive_time):  
	    dupa=format_time(arrive_time)
	    print(calculating_time(dupa))
    else:       
        print('Invalid time format, please enter in this pattern HH:MM ')
