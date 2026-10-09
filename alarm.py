import datetime
import time
import os
import pygame


def set_alarm():
    print("--- Python Alarm Clock ---")
    
    # 1. Get a valid time from the user
    while True:
        time_input = input("Enter alarm time in 24-hour format (HH:MM): ")
        try:
            # Validate format and split hours and minutes
            input_hour, input_minute = map(int, time_input.split(":"))
            if 0 <= input_hour < 24 and 0 <= input_minute < 60:
                break
            else:
                print("Invalid range. Hours must be 0-23, Minutes must be 0-59.")
        except ValueError:
            print("Invalid format. Please use HH:MM (e.g., 07:30 or 18:15).")
            
    print(f"Alarm successfully set for {input_hour:02d}:{input_minute:02d}...")

    # 2. Main tracking loop
    pygame.mixer.init()
    sound_file = "sound.mp3"  
    
    while True:
        now = datetime.datetime.now()
        
        # Check if current hour and minute match the target alarm time
        if now.hour == input_hour and now.minute == input_minute:
            print("\n WAKE UP! The alarm is ringing! ")

            if os.path.exists(sound_file):
                pygame.mixer.music.load(sound_file)
                pygame.mixer.music.play(-1)  # -1 loops the music indefinitely
                
                input("Press Enter to stop the alarm...")
                pygame.mixer.music.stop()
            else:
                print(f"[Sound file '{sound_file}' not found, just printing alert!]")
                input("Press Enter to dismiss...")
            break
            
        # Wait 10 seconds before checking again to preserve CPU resources
        time.sleep(10)

if __name__ == "__main__":
    set_alarm()
