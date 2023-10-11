from scipy.integrate import quad
import keyboard
import time

w_pressed = False
start_time = 0

while True:

    if keyboard.is_pressed("w"):
        if not w_pressed:
            w_pressed = True
            start_time = time.time()
    else:
        if w_pressed:
            w_pressed = False
            end_time = time.time()
            T = end_time - start_time
            print(f"Time = {T:.2f}")

    time.sleep(0.01)

def v(T):
    def g(t,k,n):
        return k*(t**n)
    k = 4
    n = 2
    v = quad(g, 0, T, args=(k,n))
    return v
