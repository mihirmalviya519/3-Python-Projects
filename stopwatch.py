import time
import os
import threading
from playsound3 import playsound

hours = 0
minutes = 0
seconds = 0
flag = True

def run():
    global hours,minutes,seconds,flag

    while flag:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Press ENTER to stop....")
        print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

        time.sleep(1)

        if flag:
            seconds = seconds + 1
            if(seconds == 60):
                minutes = minutes + 1
                seconds = 0

            if(minutes == 60):
                hours = hours + 1
                minutes = 0

        
stopwatch = threading.Thread(target=run)
stopwatch.start()
input()
flag = False
stopwatch.join()

print(f"Stopwatch run for : {hours:02d}:{minutes:02d}:{seconds:02d}")

sound = playsound('sound.mp3',block=False)
time.sleep(5)
sound.stop()


