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
1.入侵偵測系統  
2.rfid設備寫入與讀取  
3.投票智能合約與網站架設  


因此在開始前，我們要先安裝利用區塊鏈所需的metamask跟網頁所需的nginx

### 3-1.metamask安裝
區塊鏈的部分我們採用 ethereum 與 metamask 的組合，這邊就必須要解釋甚麼是 ethereum

####ethereum&metamask
* ethereum  
跟Bitcoin(比特幣)很像，但其多了一個功能我們稱之為叫做智能合約,而智能合約有一個作用就是我們可以支付一部分的加密貨幣，儲存、修改智能合約上的部分資訊。並且由於智能合約可在每個以太坊的節點上執行並進行驗證，因此是不可能竄改的
[image](https://user-images.githubusercontent.com/62298086/148271090-54d74fc5-3746-4b29-b8fd-ae3cc0b18ba9.png)
* metamask  
是用於與以太坊區塊鏈進行交互的軟體加密貨幣錢包。它允許用戶通過瀏覽器擴展程序或行動應用程式訪問其以太坊錢包




### 3-2.nginx安裝


##建立



##參考連結
* 區塊鏈: https://gasolin.gitbooks.io/learn-ethereum-dapp/content/what-is-smart-contract.html#fn_1



