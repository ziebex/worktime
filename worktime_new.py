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

arrive_time = input('Your time: ')

if len(arrive_time) <= 2:
	correct_time = input('Please enter your time in this format HH:MM ')
	dupa=format_time(correct_time)
	print(calculating_time(dupa))
else:
	dupa1 = format_time(arrive_time)
	print(calculating_time(dupa1))
