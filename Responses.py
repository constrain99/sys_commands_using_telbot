from datetime import datetime
import os
import pyautogui as pt
from time import sleep

def sample_responses(input_text):
    user_message=str(input_text).lower()

    if user_message in ("hloo","hello","hi","hey"):
        return "hey,how r u"

    if user_message in ("who are u"):
        return 'i am a bot'

    if user_message in ('time','time?'):
        now=datetime.now()
        date_time=now.strftime("%d/%m/%y,%H:%M:%S")

        return str(date_time)
    if user_message in ('shutdown','St','Shutdown'):
        os.system("shutdown /s /t 1")
        return 'shutdown sucessful'

    



    return "i dont understand u"