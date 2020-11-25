def F(x,y):
    return x*2 + y*2
def G(x,y):
    return x+y-3
#def L(x,y,a):
#    return x*2 + y*2 + a*(x+y-3)
def Fx(x):
    return 2*x
def Fy(y):
    return 2*y
x = 5
y = 3
c = 19
for i in range(10000):
    for j in range(1000):
        x = x-0.3*(2*x+c)
        y = y-0.3*(2*y+c)
        #if abs(Fx(x)+Fy(y)) < 0.001:
         #   break
    c = c+0.003*(x+y-3)
    print("c = ",c)