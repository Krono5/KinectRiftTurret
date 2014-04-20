str(raw_input())
str(raw_input())
str(raw_input())
str(raw_input())

import serial

ser = serial.Serial('\\.\COM6', 9600)

ser.close()
ser = serial.Serial('\\.\COM6', 9600)

while True:
  try:
    inx = str(raw_input())
    if ':' not in inx:continue
    Q = inx.split(':')
    Q = map(lambda x:x.split(',')[0],Q)[1:]
    yaw = 256.0 * ((int(Q[0]) + 180) / 360.0) - 1
    yaw = chr(int(yaw))
    print ord(yaw)
    ser.write(yaw)
  except:
    ser.close()
    raise
