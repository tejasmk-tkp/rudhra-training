import serial as sl

motor_driver = sl.Serial("/dev/ttyUSB0", 9600)

print('''Motor 1: 1 is full reverse, 64 is stop and 127 is full forward.
Motor 2: 128 is full reverse, 192 is stop and 255 is full forward.''')

val = int(input("Enter Value: "))
val = bytes([val])
print(val)

motor_driver.write(val)
