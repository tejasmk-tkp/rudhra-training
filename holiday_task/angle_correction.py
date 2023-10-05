import random as rn
from time import *

noise = rn.gauss(0, 15)

sp = int(input("Enter Target Angle: "))

pv = sp + noise

Kp, Ki, Kd = 1, 0, 0

e = sp - pv

print(sp, pv, e)

prev_e = 0
integral = 0

while pv != sp:

    P = Kp*e

    integral += e
    I = Ki*integral

    D = Kd*(e-prev_e)
    prev_e = e

    pv = P + I + D

    e = sp - pv

    print(sp, pv, e)

    sleep(1)

