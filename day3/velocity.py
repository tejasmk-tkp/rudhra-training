def g(t):
    r = 1
    a = r*t    
    return a

def v(t):
    v = t * g(t)
    return v

t=int(input("Time: "))
print(v(t))
