import RPi.GPIO as GPIO
import time
from picamera import PiCamera 
from time import sleep 
from datetime import datetime
 
#初始化
def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12,GPIO.IN)
    GPIO.setup(26,GPIO.OUT)
    pass
 
#蜂鳴器鳴叫函數
def beep():
    while GPIO.input(12):
        GPIO.output(26,GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(26,GPIO.HIGH)
        time.sleep(0.5)
#紅外線感應器偵測函數
def detct():
    #因為是僅僅試驗，所以只讓它循環運行100次
    camera = PiCamera() 
    for i in range(1,101):
        #如果感應器針腳輸出為True，則印出離開警告信息並執行蜂鳴器與拍照
        if GPIO.input(12) == True:
            print ("Someone isclosing!")
            beep()
            #呼叫相機進行拍照，名稱為當下的年月日，將照片存於桌面的camera_image資料夾中
            localtime = time.localtime()
            result = time.strftime("%Y%m%d%I%M%S%p", localtime)
            camera.start_preview()
            sleep(1)
            camera.capture('/home/pi/Desktop/camera_image/image'+ str(result) +'.jpg')
            camera.stop_preview()
        #否則將蜂鳴器的針腳電平設置為HIGH(也就是不會有聲音的意思)
        else:
            GPIO.output(26,GPIO.HIGH)
            print ("Noanybody!")
            time.sleep(2)
 

init()
detct()
#腳本運行完畢執行清理工作
GPIO.cleanup()
  
