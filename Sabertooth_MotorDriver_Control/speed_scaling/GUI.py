from tkinter import *
import serial as sl

motor_driver = sl.Serial("/dev/ttyUSB0", 9600)

def map_range(value, from_low, from_high, to_low, to_high):

    value = int(value)

    normalized_value = (value - from_low)/(from_high - from_low)

    mapped_value = round(to_low + normalized_value * (to_high - to_low))

    return max(to_low, min(to_high, mapped_value))

def send_data(data):
    #if value != 0:
    store = data
    data = map_range(data, 0, 100, 0, 255)
    print(store, data)
    data = int(data)
    data = bytes([data])
    motor_driver.write(data)

root = Tk()
root.title("Speed Scaling")

data = IntVar()

data_label = Label(root, text="Speed Slider")
data_label.pack(pady = 10)

slider = Scale(root, from_ = 0, to = 100, variable = data, orient = "vertical", length = 510, sliderlength = 40, command = send_data)

slider.pack()

root.mainloop()

