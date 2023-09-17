from scipy.integrate import quad

def v(T):
    def g(t,k,n):
        return k*(t**n)
    k = 4
    n = 2
    v = quad(g, 0, T, args=(k,n))
    return v
