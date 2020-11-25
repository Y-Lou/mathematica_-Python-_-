def F(x,y,z):
	return 3*x**4+7+4*y**4+9+6*z**4+8
def G(x):
	return 12*x**3
def H(y):
	return 16*y**3
def K(z):
	return 24*z**3
x = 12
y = 23
z = 45
i = 0
#for i in range(100000):
while True:
	x = x - 0.0006*G(x)
	y = y - 0.00022*H(y)
	z = z - 0.000036*K(z)
	i += 1
	print("x,y,z = ",[x,y,z])
	print("*"*20)
	print("F = ",F(x,y,z))
	print("cishu = ",i)
	if abs(G(x)+H(y)+K(z)) < 0.001:
		break 