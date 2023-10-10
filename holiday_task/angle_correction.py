import random as rn
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def PID(Kp, Ki, Kd, setpoint, feedback):
    
    time = 0
    time_prev = -1e-6
    I = 0
    e_prev = 0

    e = setpoint - feedback
    #print(e)    
    P = Kp*e
    I += Ki*e*(time - time_prev)
    D = Kd*(e - e_prev)/(time - time_prev)
    #print(P, I, D)
      
    Output = P + I + D

    e_prev = e
    time_prev = time

    return Output

noise = rn.gauss(0, 15)
setpoint = int(input("Enter Target Angle: "))
feedback = setpoint + noise
error = setpoint - feedback
print("Setpoint", "Feedback", "Error")
print(setpoint, feedback, error)

while feedback != setpoint:
    output = PID(1, 0.01, 0, setpoint, feedback)
    #print(output)
    feedback = feedback+output
    #print(feedback)
    error = setpoint - feedback
    print(setpoint, feedback, error)

print("Target Achieved")
