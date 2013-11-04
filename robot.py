import serial

ser = serial.Serial('/dev/ttyS0',baudrate=19200 )
ser.close()
ser.open()

ser.write("\x80") # 128: start command
ser.write("\x82") # 130: control command
ser.write("\x87") # 135: clean command
ser.flush()
ser.close()
