# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time,spidev
import paths
from datetime import datetime as dt
from datetime import date, timedelta


#MCP3002からSPI通信で10ビットのデジタル値を取得。0から１の２チャンネル利用可
def readadc_spidev(adcnum):
    if ((adcnum > 1) or (adcnum < 0)):
        return -1

    command1 = 0xd | (adcnum<<1)
    command1 <<= 3
    ret = spi.xfer2([command1,0,0])
    adcout = (ret[0]&0x3)<<8 | ret[1]
    return adcout

def writefile():
    dt_now = dt.strftime(dt.now(), '%Y-%m-%d %H:%M:%S')
    today = dt.strftime(dt.today(), '%Y-%m-%d')
    path_timelog = paths.timelog+ str(today)
    with open(path_timelog,mode='a') as f:
        f.write((str(dt_now) + '\n'))
        f.close() 
    

GPIO.setmode(GPIO.BCM)
spi=spidev.SpiDev()
spi.open(0, 0) # bus0, CE0
spi.max_speed_hz = 1000000  # 1MHz


try:
    while True:
        inputVal0 = readadc_spidev(0)
        print(inputVal0)
        if inputVal0 > 100:
            writefile()
        time.sleep(10)

except KeyboardInterrupt:
    pass

spi.close()
