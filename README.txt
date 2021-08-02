if you cant play the music O.wav, you should change the chunk. i first set the chunk 1024 on Ubuntu Linux. then now i set the chunk as 2048 on Ubuntu Mate with RaspberryPi.

chunk 1024 -> 2048

vi /home/users/.asoundrc
. asoundrc파일작성있어야 라즈베리파이에서USB 마이크로 작동합니다.


How to play
PC
git clone https://github.com/jleb/pyaudio.git
python3 setup.py install
so 파일 옮기기 :  cd build/lib.linux-x86_64-3.8
cp _portaudio.cpython-38-x86_64-linux-gnu.so ../../../LOOP/venv/lib/python3.8/site-packages/
pip3 install Adafruit-CharLCD==1.1.1


Raspberry
sudo apt-get install python3-rpi.gpio


Reference
Adafruit_CharLCD : https://github.com/adafruit/Adafruit_Python_CharLCD/
pyaudio : https://github.com/jleb/pyaudio.git

