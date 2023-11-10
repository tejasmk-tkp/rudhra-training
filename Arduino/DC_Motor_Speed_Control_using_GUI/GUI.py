from tkinter import *
import serial as sl

arduino = sl.Serial("/dev/ttyUSB0", 9600)

def send_PWM(value):
    value = bytes([int(value)])
    arduino.write(value)

root = Tk()
root.title("DC Motor Speed and Direction Control")

PWM = IntVar()

PWM_label = Label(root, text="Speed and Direction Slider")
PWM_label.pack(pady = 10)

slider = Scale(root, from_ = 0, to = 255, variable = PWM, orient = "vertical", length = 510, sliderlength = 40, command = send_PWM)

slider.pack()

root.mainloop()
