from datetime import datetime
from datetime import date
from datetime import timedelta
todays_date = date.today() #print todays date
print("Today's date is",todays_date)

print("Year is",todays_date.year,"Month is ",todays_date.month,"Day is",todays_date.day)

todays_datetime = datetime.now()#print date and time of present condition
print("The currnet date and time is ",todays_datetime)

time = datetime.time(todays_datetime)#print time of present condition
print("Time is ",time)

#Printing the day of week
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
weekendday = date.weekday(todays_date)
print("Today is ",days[weekendday])

#print the datetime in formatted way
print(todays_date.strftime("%A,%d %B,%Y"))

print(todays_date.strftime("%c"))#prints the local date and time
print(todays_date.strftime("%x"))#prints the local date
print(todays_date.strftime("%X"))#prints the local time

#print(todays_date.strftime("%H:%M:%S %P"))

#Use of timedelta function
#With timedelta objects, you can estimate the time for both future and the past.
# In other words, it is a timespan to predict any special day, date or time.

#To find final date after 768 days from present  using timedelta function

print("The date from after 768 days is ",str(todays_datetime + timedelta(days=768)))


