"""Note:- You have to run and close this file manually through cmd  from client pc"""
import pyautogui
import cv2
import numpy as np
from datetime import datetime
import time
import getpass


class ScreenRecorder:
    @classmethod
    def record(cls, stop):
        user = getpass.getuser()

        start = time.time()

        width = pyautogui.size().width
        height = pyautogui.size().height
        SCREEN_SIZE = (width, height)

        fourcc = cv2.VideoWriter_fourcc(*"XVID")

        video_name = str(datetime.today()).strip().split('.')[0].replace(':', '-').replace(' ', '_') + '.avi'
        out = cv2.VideoWriter(f'C:\\User\\{user}\\Python\\screen_recordings\\{video_name}', fourcc, 10.0, (SCREEN_SIZE))

        while True:
            end = time.time()
            if end - start >= stop:
                break

            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame)

            if cv2.waitKey(1) == 27:
                break

        cv2.destroyAllWindows()
        out.release()

