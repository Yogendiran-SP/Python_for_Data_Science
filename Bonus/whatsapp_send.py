import pywhatkit as pwk
import datetime
import time
import pyautogui

number = "+916380184609"
msg="Hello Jai from Python!.... (without using selenium)"

now=datetime.datetime.now()

sendhr=now.hour
sendmt=now.minute + 2

try:
    pwk.sendwhatmsg(number,msg,sendhr,sendmt)

    time.sleep(20)
    pyautogui.press("enter")

except:
    print("Error")
    
else:
    print("✅Message sent successfully!")