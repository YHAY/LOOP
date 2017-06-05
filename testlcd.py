from Adafruit_CharLCD import Adafruit_CharLCD
from time import sleep
#ln -s "Adafruit path" Adafruit_CharLCD
lcd = Adafruit_CharLCD(rs=22, en=11, d4=23, d5=10, d6=9, d7=25, cols=16, lines=2)
count = 0
while True:
  lcd.clear()
  lcd.message(str(count) + 'st Recording')
  sleep(1)
