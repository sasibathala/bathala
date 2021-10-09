# Python program to Find day of
# the week for a given date
import datetime
import calendar
from collections import OrderedDict

def findDay(date):
	born = datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
	return (calendar.day_name[born])


D = {'2020-01-01' : 4,'2020-01-02' : 4 ,'2020-01-03' : 6 ,'2020-01-04' : 8 ,
    '2020-01-05' : 2 , '2020-01-06' : 6 ,'2020-01-07' : 2,'2020-01-08' : 2 }
    
#list1 = [findDay(i) for i in D.keys() ]
newdic = {}
for i,j in D.items():
    newdic[findDay(i)] = j
print(newdic)   

m = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday","Sunday"]
n = newdic.keys()
x = sorted(n, key=m.index)
print(x)
