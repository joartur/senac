a = 2
b = 2
c = 3

delta = b**2 - 4*a*c

print("O valor de delta é: " + str(delta))

if delta > 0:
    
    x1 = (-b + (delta*0.5)) / (2*a)
    x2 = (-b - (delta*0.5)) / (2*a)
    print(f"As raízes são: x1 = {x1}, x2 = {x2}")
elif delta == 0:
    
    x1 = -b / (2*a)
    print(f"A raiz é: x1 = {x1}")