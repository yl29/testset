# print out what the weekday of a given date
import time
import datetime
def print_weekday(p1, p2, p3, num):
    output = str(p1)+"/"+str(p2)+"/"+str(p3)+" is: "
    weekday = {1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday',5:'Friday', 6:'Saturday', 0:'Sunday'}
    print output+weekday[int(num)]

year = [i for i in range(1982,2082)]
month = 6;day = 4
for y in year:
    anyday=datetime.datetime(y,month,day).strftime("%w")
    print_weekday(y,month,day,anyday)
