import random as rn
import matplotlib.pyplot as plt
import time

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
#error = setpoint - feedback
print("Setpoint", "Feedback")
print(setpoint, feedback)

time_val = []
feedback_val = []
setpoint_val = []

start_time = time.time()

while feedback != setpoint:
    noise = rn.gauss(0, 15)
    output = PID(1, 0.01, 0, setpoint, feedback)
    #print(output)
    feedback += output + noise
    #print(feedback)
    #error = setpoint - feedback
    time_val.append(time.time() - start_time)
    feedback_val.append(feedback)
    setpoint_val.append(setpoint)
    print(setpoint, feedback)

    plt.clf()
    plt.plot(time_val, feedback_val)
    plt.plot(time_val, setpoint_val, 'r-')
    plt.grid()
    plt.pause(0.1);

    time.sleep(0.1);

print("Target Achieved")
