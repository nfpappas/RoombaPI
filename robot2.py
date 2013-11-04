import serial
import time

ser = serial.Serial(0,baudrate=19200,timeout=0.1)
ser.close()
ser.open()
#wake up robot
ser.setRTS(0)
time.sleep(0.1)
ser.setRTS(1)
time.sleep(2)

#pulse device-detect 3 times
for i in range(3):
   ser.setRTS(0)
   time.sleep(0.25)
   ser.setRTS(1)
   time.sleep(0.25);
