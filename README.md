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
#### 1.入侵偵測系統  
#### 2.rfid設備寫入與讀取  
#### 3.投票智能合約與網站架設  


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
#### 1.入侵偵測系統  
#### 2.rfid設備寫入與讀取  
#### 3.投票智能合約與網站架設  


### 1.入侵偵測系統  
這邊需安裝三項東西１．蜂鳴器　２．紅外線感測器　３．鏡頭　　
運行腳本後，感應模塊每隔一定時間檢測，如有人靠近，則發出嗶嗶報警聲，並在屏幕印出提示信息，並且進行拍照（檔案存於本機端），人若離開，則停止鳴叫

請先命名一個python檔，程式碼如下

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
        #否則將蜂鳴器的針腳電平設置為HIGH(也就是不會有聲音的意思)
        else:
            GPIO.output(26,GPIO.HIGH)
            print ("Noanybody!")
            time.sleep(2)
 

init()
detct()
#腳本運行完畢執行清理工作
GPIO.cleanup()
  
```

### 2.RFID設備寫入與讀取
此設備利用RFID-RC522模組對rfid設備進行感測，並呼叫本機端的網頁  
首先我們必須要安裝rfid的套件

#### 安裝RFID套件
在開始在 Raspberry Pi 上使用 RFID RC522 的過程之前，首先必須對其配置進行更改。默認情況下，Raspberry Pi 禁用了 SPI（串行外設接口），請先在終端機打上以下指令更改 SPI

##### 環境設置
1.輸入指令  
```
sudo raspi-config
```
2.在此處使用箭頭鍵選擇"5 Interfacing Options"。選擇此選項後，按Enter。  

3.現在在下一個屏幕上，您要使用箭頭鍵選擇 "P4 SPI "，再次按 Enter 選擇該選項

4.現在將詢問您是否要啟用 SPI 接口，使用箭頭鍵選擇是，然後按Enter繼續。當raspi- config 工具開始啟用 SPI時，需要稍等一下。  

5.使用raspi-config工具成功啟用 SPI 接口後，您應該會在屏幕上看到以下文字，" SPI 接口已啟用 "。  

在 SPI 接口完全啟用之前，我們首先必須重新啟動 Raspberry Pi。 重啟後這樣就大功告成啦!  

##### 套件安裝
接下來我們就可以開始要來設置SPI接口以及RFID的讀取套件
```
sudo pip3 install spidev
sudo pip3 install mfrc522
```

#### 撰寫程式-rfid設備寫入
我們的系統會先把讀取到的RFID的ID寫入TXT檔中，以便後續可以政身分
請先命名一個python檔，程式碼如下
```python
from time import sleep
import sys
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()

try:
    while True:
        print("add to this vote")
        id, text = reader.read()
        text = 'you are vote student'
        print("ID: %s\nText: %s" % (id,text))
        sleep(5)
        #寫入TXT檔以便橫續讀取認證
        path = 'output.txt'
        f = open(path, 'a')
        
        student_id = str(id)
        f.write(student_id)
        f.close()
        
        print("id= ",id)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    raise

```

#### 撰寫程式-rfid設備讀取
讀取TXT檔，找出ID，並呼叫本機端的網頁，程式碼如下
```python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import webbrowser  
reader = SimpleMFRC522()
try:
    id, text = reader.read()
    #open txt get all voters
    path = 'output.txt'
    f = open(path, 'r')
    all_voters = f.read()
    f.close()
    rfid_mount = 12
    len_vote = range(int(len(all_voters)/rfid_mount))
    print(len_vote)
    voters = []
    #compare rfid and student_all rfid on txt
    for i in len_vote:
        voters.append(all_voters[i*rfid_mount:(i+1)*rfid_mount])
        if str(id)==voters[i] :
            webbrowser.open('127.0.0.1', new=2)       
finally:
        GPIO.cleanup()
```

### 3.投票智能合約與網站架設 
#### 投票智能合約
我們利用Ethereum的智能合約取代資料庫，因此必須要先撰寫智能合約，合約的建置如下
1.首先要去[remix](https://remix.ethereum.org/) 建立智能合約，要注意合約的版本號要跟我寫的一樣，要不然會出問題(不同版本的變動很大)
```go
//合約版本
pragma solidity ^0.4.26;
//合約，如果要寫入變數的話必須要先行宣告(例如unit)，因為會關係到是否要付費進行合約編寫
contract ez_vote  {
    uint votes1 = 0;
    uint votes2 = 0;
   function set_a( uint _votes1) public {
       votes1 = _votes1;
   }

   function set_b( uint _votes2) public {
       votes2 = _votes2;
   }
//如果要讀取資料的話使用view，並不會花費
function get_a() public view returns ( uint) {
       return (votes1);
   }  
   function get_b() public view returns ( uint) {
       return (votes2);
   }  
}  
```
按下compile  
![image](https://user-images.githubusercontent.com/62298086/148498107-0460c2e7-25aa-4c46-be74-428bf6dab40f.png)  

部屬合約，你可以選擇部屬在jvm上測試合約是否沒問題(類似測試環境)，一旦確認沒甚麼問題後就可以部屬在web3.js中，web3的作用是提供metamask與chrome相連的一個api  
![image](https://user-images.githubusercontent.com/62298086/148498575-b702fa30-d257-4746-a40d-9a4ad086b5b5.png)  
部屬完後，可以從你的metamask中找出合約地址，將其複製到記事本等等會用到  
![image](https://user-images.githubusercontent.com/62298086/148498972-e0e44be8-aabf-4734-a1c3-319b988753b9.png)  
![image](https://user-images.githubusercontent.com/62298086/148499036-aef95b85-4389-4e49-8dc4-688228848fdf.png)  

複製ABI(一種你的智能合約轉給機器看得code)，等等我們網站會用到  
![image](https://user-images.githubusercontent.com/62298086/148499725-46e1959b-0600-4cee-95b7-50e980e88abb.png)  


#### 網站架設 
前面我們已經把網站伺服器架設完成，因此我們要來寫一個簡單的投票網站
大致上如下，需要更改的地方就是ABI與合約地址的部分，改完網站即可使用
```php
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title></title>
	<link rel="stylesheet" type="text/css" href="index_html.css">
</head>

<body>
<div class="textstyle1">
  <div id="text_54a1c552">
    <div class="textstyle1">
      <span class="textstyle2">A候選人</span>
        <br>目前票數<input type="text" id="quantity1" readonly="true">
        <br><button id="more1" type="button">選擇他</button>
    </div>
    </div>
  <div id="text_1fd9e86b">
    <div class="textstyle1">
      <span class="textstyle2">B候選人</span>
      <span class="textstyle2">A候選人</span>
        <br>目前票數<input type="text" id="quantity2" readonly="true">
        <br><button id="more2" type="button">選擇他</button>
    </div>
    </div>
  </div>
<div class="textstyle3">
<span class="textstyle4"><br/></span><span class="textstyle5">學生會長選舉</span>  </div>
<div class="textstyle1">
  <img src="rc_images/323fcac99ac5w815h1019.jpeg" id="img_4813649a" alt="" title="" />
  <img src="rc_images/6b4bd691_fe83_49f4_8c2e_00fffadad9e7.jpg" id="img_3bca5026" alt="" title="" />



<<!--後端 web3的應用-->
<script src="https://code.jquery.com/jquery-3.1.0.min.js"></script>
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/web3/1.3.4/web3.min.js"></script>
<script>
    if (typeof web3 !== 'undefined') {
        web3 = new Web3(web3.currentProvider);
    } else {
        // set the provider you want from Web3.providers
        web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8545"));
    }
	//利用ABI與合約地址讀取合約,需要更改合約地址與ABI code即可執行
    var CoursetroContract = new web3.eth.Contract(
       [//把剛複製的ABI貼在這邊
    {
        "constant": false,
        "inputs": [
            {
                "name": "_votes2",
                "type": "uint256"
            }
        ],
        "name": "set_b",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "get_a",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "_votes1",
                "type": "uint256"
            }
        ],
        "name": "set_a",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "get_b",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    }
]
        , '0xd857cdaa0b7da81c3d8ac9fe7ca63780134b41f4'//合約地址
    );
    /*pragma solidity ^0.4.26; contract ez_vote  { uint votes1 = 0; uint votes2 = 0; function set_a( uint _votes1) public { votes1 = _votes1; } function set_a() public view returns ( uint) { return (votes1); } function get_b( uint _votes2) public { votes2 = _votes2; } function get_b() public view returns ( uint) { return (votes2); } }*/
    window.history.forward(1);
     async function initContractLogic() {
        var currentAccounts = await web3.eth.getAccounts();

        $('#more1').on('click', function() {
            var yes = confirm('你確定嗎？');
            if (yes) {
                alert('你已進行投票');
                var qtt1 = parseInt($('#quantity1').val(), 10);//增加票數
                $('#quantity1').val(qtt1+1); //增加票數
                CoursetroContract.methods.set_a($('#quantity1').val().trim()).send({from: currentAccounts[0]}).on('transactionHash', function(hash){
                    console.log('hash', hash);
                }).on('confirmation', function(confirmationNumber, receipt) {
                    updateHtmlData();
                }).catch(function(error) {
                    console.log(error, 'error');
                });

                
                setTimeout("location.href='/end.html'",2000);

            } else {
                alert('你選擇取消');
            }
            
        });  

        $('#more2').on('click', function() {
            var yes = confirm('你確定嗎？');
            if (yes) {
                alert('你已進行投票');
                var qtt2 = parseInt($('#quantity2').val(), 10);//增加票數
                $('#quantity2').val(qtt2+1); //增加票數
                CoursetroContract.methods.set_b($('#quantity2').val().trim()).send({from: currentAccounts[0]}).on('transactionHash', function(hash){
                    console.log('hash', hash);
                }).on('confirmation', function(confirmationNumber, receipt) {
                    updateHtmlData();
                }).catch(function(error) {
                    console.log(error, 'error');
                });
                 setTimeout("location.href='/end.html'",2000);
            } else {
                alert('你選擇取消');
            }
        });  
       

        function updateHtmlData() {

            CoursetroContract.methods.get_a().call(function(error, result){
                if (error) {
                    console.log(error, 'error')
                } else {
                    console.log(result, 'result');
                    $('#quantity1').val(result);
                }
            });
            CoursetroContract.methods.get_b().call(function(error, result){
                if (error) {
                    console.log(error, 'error')
                } else {
                    console.log(result, 'result');
                    $('#quantity2').val(result);
                }
            });
        }
        updateHtmlData();
    }
    initContractLogic();
</script>

</body>
</html>
```
這樣就大功告成了!

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






