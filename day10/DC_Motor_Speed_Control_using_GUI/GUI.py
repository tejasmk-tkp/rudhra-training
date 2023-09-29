from tkinter import *
import serial as sl
import struct

arduino = sl.Serial("/dev/ttyACM0", 9600)

def send_PWM(value):
    value = int(value)
    value = struct.pack('i', value)
    arduino.write(value)

root = Tk()
root.title("DC Motor Speed and Direction Control")

PWM = IntVar()

PWM_label = Label(root, text="Speed")
PWM_label.pack(pady = 10)

slider = Scale(root, from_ = 0, to = 255, variable = PWM, orient = "vertical", length = 300, sliderlength = 40, command = send_PWM)

slider.pack()

dir_label = Label(root, text="Direction")
dir_label.pack(pady = 30)



root.mainloop()
