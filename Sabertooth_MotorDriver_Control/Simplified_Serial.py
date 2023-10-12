import serial as sl

motor_driver = sl.Serial("/dev/tty0", 9600)

print('''Motor 1: 1 is full reverse, 64 is stop and 127 is full forward.
Motor 2: 128 is full reverse, 192 is stop and 255 is full forward.''')

lst = []
val = int(input("Enter Value: "))
lst.append(val)
print(lst)
val = bytes(lst)
print(val)
print(len(val))

motor_driver.write(val)

if KeyboardInturrupt:
    ser.close()
