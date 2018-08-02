# Python-Google-Translate

## Dependencies:
  1. Python 3
  2. dlib (Required to install face_recognition)
  3. face_recognition
  4. Telegram API
  5. BeautifulSoup

## Hardware Dependencies
  1. Arduino
  2. L293D IC
  3. DC Motor
  4. Connecting Wires
  5. DC Power Supply
 
## Installation for Python 3
Visit: https://www.python.org/downloads/ and download the version suitable for your System
  
## Installation for face_recognition
This module is tough to install as installing dlib, which is a dependency for this module is quite challenging.
Linux users may have some easy in installation as they can use pip to install them directly. 
But windows users are recommended to go through the following tutorial for the installation process.

https://github.com/ageitgey/face_recognition/issues/175#issue-257710508

Other useful links are listed below:
  1. https://pypi.org/project/dlib/
  2. https://pypi.org/project/face_recognition/
  
## Installation for Telegram API
Open Command Prompt (Windows) or Terminal (Linux) and type in the following command:
     
     pip install python-telegram-bot
  
Visit: https://python-telegram-bot.org/
  
## Installation for BeautifulSoup
Open Command Prompt (Windows) or Terminal (Linux) and type in the following command:
     
     pip install bs4
  
Visit: https://www.crummy.com/software/BeautifulSoup/

## Interfacing Arduino
The arduino used here is Arduino Uno and is programmed with Arduino IDE.
Further information can be found in the following link.
https://www.arduino.cc/
 
## L293D IC
This is a motor driver IC which is primarily used to pass high-current and high-voltage to the motor but control the inputs depending on the signals from the Arduino.
Since the Arduino is restricted to supplying of 5V and cannot meet the current requirement to drive a DC motor, L293D IC has been used.
The IC Datasheet can be found at http://www.ti.com/lit/ds/symlink/l293.pdf

## DC Power Supply
For this, any 5-12 volts power supply can be used. For the purpose of this project, we have used Smartphone Charger.

## How to use?
  1. Program the Arduino with the given code
  2. Connect the wires and set up as shown in the circuit diagram
  3. Create an account in way2sms (http://www.way2sms.com/)
  4. Create a Telegram bot using BotFather
  5. Add the missing credentials and Token in the python files (face_recg.py and TelegramAPI.py)
  6. Add a well lit picture of the person whose face has to be recognized in the Assets folder and change face_recg.py accordingly
  6. Run the TelegramAPI.py and keep it running
  7. Run the face_recg.py when ready for facial recognition
  8. Interact with the bot with the given commands
  9. To get started, you can send /help to the bot
