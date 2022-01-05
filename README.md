# 含入侵偵測系統的實體電子投票機


## 一、概述
此篇文章會教你建設一個並且含入侵偵測系統與利用區塊鏈取代傳統資料庫一個實體電子投票機，此機器主要有兩個功能  
1.入侵偵測驅趕:如果有人開投票機，紅外線一感應到人，會有攝像頭進行拍攝，蜂鳴器進行驅趕  
2.身分驗證投票:感應rdid設備(例如:學生證)，並利用區塊鏈進行投票

### 軟硬體應用項目
* 硬體方面: 
  * 樹梅派: 控制RC522RFID模組進行讀取身分驗證卡、
  * 蜂鳴器、紅外線感測器、攝像機模組: 以防有人對投票機進行偷竊或修改  
* 軟體方面: 
  * nginx: 架設網站，
  * metamask: 用來與區塊鏈的資訊進行交易與讀取
  * remix: 撰寫智能合約(一種利用區塊鏈不可竄改性的程式)以儲存選票

### 使用情境  
例如學生會要選出學生會長或者是班長的選舉，可透過學生証，並利用該投票機進行投票 

### 此系統的特色
此系統具有相當的安全性，可以從硬體與軟體方面說明
* 硬體方面:如果有人想要從機器上對其進行選票的修改，會有蜂鳴器進行驅趕，並且拍照留底
* 軟體方面:利用區塊鏈取代資料庫，如果對單一節點進行修改，因為區塊鏈的特性其他的電腦會驗證其正確性，因此無法做到資料的篡改





## 二、Components
### 硬體
* Raspberry Pi 3  *1
* RFID-RC522模組 (含卡、感應鑰匙) 
* 蜂鳴器 *1
* 紅外線感測器 *1
* 鏡頭模組 *1
* 灰紙板 *1

### 軟體
*Python 3.7
*nginx
*metamask

## 三、電路圖
![image](https://user-images.githubusercontent.com/62298086/147538187-cd7c4f6c-cd86-407e-8d2f-ccdb890a965d.png)
Transistor 可以選擇裝或不裝，它的作用是用來控制蜂鳴器的叫聲
注意!此電路圖不包含鏡頭



## 四、流程圖





## 五、開始之前
我們會將這個系統拆成三個部分去做執行分別為  
### 1.入侵偵測系統  
### 2.rfid設備寫入與讀取  
### 3.投票智能合約與網站架設  


因此在開始前，我們要先做以下步驟:  
1.安裝與區塊鏈溝通所需的metamask  
2.網頁所需的server nginx  

### 3-1.metamask安裝
區塊鏈的部分我們採用 ethereum 與 metamask 的組合，這邊就必須要解釋甚麼是 ethereum

#### ethereum&metamask
* ethereum  
跟Bitcoin(比特幣)很像，但其多了一個功能我們稱之為叫做智能合約,而智能合約有一個作用就是我們可以支付一部分的加密貨幣，儲存、修改智能合約上的部分資訊。並且由於智能合約可在每個以太坊的節點上執行並進行驗證，因此是不可能竄改的，而在此我們用來儲存選票
* metamask  
是用於與以太坊區塊鏈進行交互的軟體加密貨幣錢包。它允許用戶通過瀏覽器擴展程序或行動應用程式訪問其以太坊錢包
![image](https://user-images.githubusercontent.com/62298086/148272749-a2221f70-8bf3-4adb-83f0-9f41dfc4d0e6.png)
#### metamask的安裝
去chrome 線上應用程式商店 尋找 metamask 依步驟安裝即可，由於我們是測試，因此將資料發佈在測試鏈上(要不然會花錢)
![image](https://user-images.githubusercontent.com/62298086/148273056-65f66565-27eb-45b5-9379-5bf19a23008c.png)

### 3-2.nginx安裝
1.使用 apt 安裝基本的 NGINX 網頁伺服器：
```
sudo apt-get install nginx    
```
2. 檢查一下這個服務的狀態，如狀態為running，可打開瀏覽器127.0.0.1 會顯示welcome to nginx 
```
service nginx status 
```








##建立
我們一樣分為三個部分進行執行
### 1.入侵偵測系統  
### 2.rfid設備寫入與讀取  
### 3.投票智能合約與網站架設  


### 1.入侵偵測系統  
這邊需安裝三項東西１．蜂鳴器　２．紅外線感測器　３．鏡頭　　
運行腳本後，感應模塊每隔一定時間檢測，如有人靠近，則發出嗶嗶報警聲，並在屏幕印出提示信息，並且進行拍照（檔案存於本機端），人若離開，則停止鳴叫
程是碼如下

```python
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
        #否則將蜂鳴器的針腳電平設置為HIGH
        else:
            GPIO.output(26,GPIO.HIGH)
            print ("Noanybody!")
            time.sleep(2)
 

init()
detct()
#腳本運行完畢執行清理工作
GPIO.cleanup()
  
```




## 參考連結　　
* 區塊鏈知識 https://gasolin.gitbooks.io/learn-ethereum-dapp/content/what-is-smart-contract.html#fn_1　　
* Rfid
https://pimylifeup.com/raspberry-pi-rfid-rc522/　　

* 蜂鳴器&紅外線感測
https://shumeipai.nxez.com/2014/08/31/infrared-sensor-module-and-buzzer-alarm-achieve.html　　

* 網站架設(nginx)
https://blog.gtwang.org/iot/raspberry-pi-install-nginx-lightweight-web-server/

* 智能合約撰寫
https://ethereum.stackexchange.com/questions/79523/how-to-get-web3-to-interact-with-smart-contract-to-input-string-info

* 網頁撰寫
https://stackoverflow.com/questions/39276635/how-to-add-1-to-a-value-in-an-input-field-with-javascript-on-click






