import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime
import os

def sign_in(meetingid ,pswd):


    # subprocess.Popen(['google-chrome'], stdout=os.open(os.devnull, os.O_RDWR), stderr=subprocess.STDOUT)
    time.sleep(5)


    # click on join
    join_btn = pyautogui.locateCenterOnScreen('join_btn.PNG')
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    # type meeting id
    # meetingid_btn = pyautogui.locateCenterOnScreen('meeting_btn.PNG')
    # pyautogui.moveTo(meetingid_btn)
    # pyautogui.click()
    pyautogui.write(meetingid)

    # disable camera and mic
    media_btn = pyautogui.locateCenterOnScreen('check_btn.PNG')
    for btn in media_btn:
        pyautogui.moveTo(btn)
        pyautogui.click()
        time.sleep(2)

    # hit join
    nxtjoin_btn = pyautogui.locateCenterOnScreen('nxtjoin_btn.PNG')
    pyautogui.moveTo(nxtjoin_btn)
    pyautogui.click()

    # password
    meeting_pswd_btn = pyautogui.locateCenterOnScreen("pswd_btn.PNG")
    pyautogui.moveTo(meeting_pswd_btn)
    pyautogui.click()
    pyautogui.write(pswd)
    pyautogui.press('enter')

# Reading the file 
df = pd.read_csv('classes.csv')

while True:
    now = datetime.now().strftime("%H:%M")
    if now in str(df['timings']):

        row = df.loc[df['timings'] == now]
        m_id = str(row.iloc[0,1])
        m_pswd = str(row.iloc[0,2])

        sign_in(m_id, m_pswd)
        time.sleep(40)
        print("Signed in")


