from tkinter import *
import serial as sl

arduino = sl.Serial("/dev/ttyACM0", 9600)

def send_data(data):
    store = data
    print(store, data)
    data = bytes([int(data)])
    print(data)
    arduino.write(data)

root = Tk()
root.title("Speed Scaling")

data = IntVar()

data_label = Label(root, text="Speed Slider")
data_label.pack(pady = 10)

slider = Scale(root, from_ = 0, to = 100, variable = data, orient = "vertical", length = 510, sliderlength = 40, command = send_data)

slider.pack()

root.mainloop()

