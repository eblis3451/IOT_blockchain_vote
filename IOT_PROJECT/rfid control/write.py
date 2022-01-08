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
