#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib import dates as mdates
from datetime import datetime as dt
from datetime import date, timedelta
import sys,paths

xlist=[]
ylist=[]


today = dt.today()
lastweek = today - timedelta(days=7)
# today = dt.strftime(today, '%Y-%m-%d')
# lastweek = dt.strftime(lastweek, '%Y-%m-%d')

for i in range(0,7):
    day = today - timedelta(days=i) 
    path = paths.timelog + dt.strftime(day, '%Y-%m-%d')
    with open(path,mode='r') as f:
        x=0
        for row in f:
            # x+=1
            # if (x%10==0):
            #     print(S) 
            S=row.strip().split()
            #print(S)
            xlist.append(S[0])
            ylist.append(S[1])

#change type into str to axis
today = dt.strftime(today , '%Y-%m-%d')
lastweek = dt.strftime(lastweek, '%Y-%m-%d')

#xlist,ylist change into datetime type
xlist = [dt.strptime(d, '%Y-%m-%d') for d in xlist]
ylist = [dt.strptime(d, '%H:%M:%S') for d in ylist]
#plot data
ax = plt.subplot()
ax.scatter(xlist,ylist)
# Xaxis (per a day)
ax.xaxis.set_major_locator(mdates.DayLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d"))
ax.set_xlim([dt.strptime(lastweek,'%Y-%m-%d'), dt.strptime(today, '%Y-%m-%d')])
#ax.set_xlim([dt.strptime('2020-8-18','%Y-%m-%d'), dt.strptime('2020-8-21', '%Y-%m-%d')])
# Yaxis (per ahour)
ax.yaxis.set_major_locator(mdates.HourLocator())
ax.yaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
ax.set_ylim([dt.strptime('00:00','%H:%M'), dt.strptime('23:59','%H:%M')])

plt.xticks(rotation=90)
plt.savefig('media'+ today +'.png')

