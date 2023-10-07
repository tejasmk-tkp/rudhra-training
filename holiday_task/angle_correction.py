import random as rn
#from time import *
import math
import matplotlib.pyplot as plt

class PIDController:
    def __init__(self, kp, ki, kd, setpoint):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.setpoint = setpoint
        self.error = 0
        self.integral = 0
        self.derivative = 0
        self.error_prev = 0

    def update(self, process_variable):
        self.error = setpoint - process_variable
        self.integral += self.error
        self.derivative = (self.error - self.error_prev)
        output = self.kp*self.error + self.ki*self.integral + self.kd*self.derivative
        self.error_prev = self.error
        return output

noise = rn.gauss(0, 15)
setpoint = int(input("Enter Target Angle: "))
processVariable = setpoint + noise
#setpoint = 10

pid_controller = PIDController(1, 0.1, 0.01, setpoint)

for t in range(100):
    measured_value = processVariable
    output = pid_controller.update(measured_value)
    error = pid_controller.error
    print(setpoint, measured_value, error, output)

plt.plot(measured_value)
plt.plot(output)
#plt.plot(setpoint)
plt.show()

'''Kp, Ki, Kd = 1, 0, 0

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
'''
