def main():
    a = 2
    b = 2
    x = 2.5
    y = 3.5
    c = f(a,b)	
    z = g(x,c)	
    x = f(int(z), b)	
    print(a, b, c)
    print(x, y, z)


def f(n,m):
    k =  n + m
    k *= 2
    return k


def g(s, n):
    return n*s


def w(a, b ,c):
    m = a+b+c
    return a+c


main()


