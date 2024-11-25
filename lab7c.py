#!/usr/bin/env python3
# Student ID:[ako7]
class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self,hour=12,minute=0,second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objests and return the sum."""
    sum = Time(0,0,0)
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second >= 60:
     sum.minute += sum.second // 60 #this will add the extra minutes from secon>
     sum.second %= 60 # this will only keep the remaining seconds

    if sum.minute >= 60:
     sum.hour += sum.minute // 60 #this will add the hours from minutes
     sum.minute %= 60 #this will only keep the remaining seconds

    if sum.hour >= 24:
     sum.hour %= 24  #this is the 24 hour format

    return sum

def change_time(self, seconds):
  """Modify the time object by adding/subtracting seconds"""
  self.second += seconds

 #This will adjust the minutes and seconds
  while self.second >= 60:
   self.second -= 60
   self.minute += 1
  while self.second < 0:
   self.second += 60
   self.minute -= 1

 #This will adjust the hours and minutes
  while self.minute >= 60:
   self.minute -= 60
   self.hour += 1
  while self.minute < 0:
   self.minute += 60
   self.hour -= 1

 #This will be within 24 hour range
  self.hour %= 24

def time_to_sec(time):
 """Converts time object to the total number of seconds from midngiht"""
 return time.hour * 3600 + time.minute * 60 + time.second

def sec_to_time(seconds):
 """Converts total number of seconds from midngiht into time object"""
 time = Time()
 minutes, time.second = divmod(seconds, 60)
 time.hour, time.minute = divmod(minutes, 60)
 time.hour %= 24 #This is within 24 hour range
 return time


def valid_time(t):
    """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True



