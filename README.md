# Python Mini Projects

Three small command-line projects built with Python, my first projects after learning several other languages. I chose Python because its libraries make it easy to build what I want.

## Requirements
pip install pygame playsound3 qrcode[pil]

The alarm clock and stopwatch play `sound.mp3`, so place an audio file with that name in the same folder as the scripts.

## 1. Alarm Clock (`alarm.py`)
Asks for a time in 24-hour format (HH:MM) and re-prompts if the input is invalid. It uses the `datetime` module to get the current time and compares it with the alarm time every 10 seconds (via `time.sleep`). When they match, `pygame` plays `sound.mp3` on a loop until you press ENTER. If the sound file is missing, it prints a text alert instead.

## 2. Stopwatch (`stopwatch.py`)
Hours, minutes and seconds start at 0. Every second, the seconds counter increases; at 60 it resets to 0 and the minutes counter increases, and the same applies from minutes to hours. The `os` module clears the terminal each second so the output doesn't pile up. A separate thread (`threading`) runs the timer so the main thread can wait for ENTER to stop it. After stopping, `playsound3` plays `sound.mp3` for 5 seconds.

## 3. QR Code Generator (`qr_code_generator.py`)
Asks for a URL and generates a QR code image using the `qrcode` library, with Pillow handling the image. The image is always saved as a PNG (a lossless format that suits QR codes) in the current working directory. `os.path.join` builds the save path, so it works the same on Windows, Mac and Linux. The `secrets` module (`token_hex`) gives each file a random name, e.g. `a3f9c21b.png`, so two generated images never overwrite each other. The full path of the saved file is printed at the end.

## Usage
python alarm.py
python stopwatch.py
python qr_code_generator.py# 3-Python-Projects
