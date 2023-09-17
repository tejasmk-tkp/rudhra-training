from scipy.integrate import quad

def g(t,k,n):
    return k*(t**n)

def v(T):
    k = 1
    n = 1
    v = quad(g, 0, T, args=(k,n))
    return v

T = int(input("Time: "))
print(v(T))
