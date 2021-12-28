# IOT_blockchain_vote
Use the blockchain voting established by iot, take the election of the student union as an example

# 概述
此篇文章會教你建設一個以區塊鏈取代資料庫並且含入侵偵測系統的一個實體電子投票機，此機器主要有兩個功能  
1.硬體方面: 利用樹梅派控制RC522RFID模組進行讀取身分驗證卡、使用蜂鳴器、紅外線感測器、攝像機模組以防有人對投票機進行偷竊或修改  
2.軟體方面: 利用nginx架設網站，並撰寫智能合約以儲存選票

## 使用情境:  
例如學生會要選出學生會長，可透過給予身分驗證卡進行驗證，並透過投票機進行投票


