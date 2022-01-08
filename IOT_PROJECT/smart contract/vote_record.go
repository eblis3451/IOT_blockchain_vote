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
