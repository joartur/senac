a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))

x1=(-b+(b**2-(4*a*c))**0.5)/(2*a)
x2=(-b-(b**2-(4*a*c))**0.5)/(2*a)

del(a)
del(b)
del(c)

print("x1=",x1)
print("x2=",x2)