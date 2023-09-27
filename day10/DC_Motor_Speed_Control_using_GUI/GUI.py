from tkinter import *
import serial as sl

root = Tk()
root.title("DC Motor Speed and Direction Control")

arduino = sl.Serial("/dev/ttyACM0", 9600)
PWM = IntVar()

label = Label(root, text="Speed")
label.pack(pady = 10)

slider = Scale(root, from_ = 0, to = 255, variable = PWM, orient = "vertical", length = 300, sliderlength = 40, command = lambda PWM_val: (label.config(text = f"PWM: {PWM_val}"), arduino.write(str(PWM_val).encode())))
slider.pack()

root.mainloop()
