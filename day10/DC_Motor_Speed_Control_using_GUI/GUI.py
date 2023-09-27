from tkinter import *

root = Tk()
root.title("DC Motor Speed and Direction Control")

PWM = IntVar()

label = Label(root, text="Speed")
label.pack(pady = 10)

slider = Scale(root, from_ = 0, to = 255, variable = PWM, orient = "vertical", length = 300, sliderlength = 40, command = lambda val: (label.config(text = f"PWM: {val}"), print(f"PWM: {val}")))
slider.pack()

root.mainloop()
