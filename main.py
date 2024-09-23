#вариант 4
import math
x=int(input("Введите x: "))
y=int(input("Введите y: "))
z=int(input("Введите z: "))
b=((10*((x**(1/3))+(x**(y+2))))**(1/2))*((math.asin(z))**2-abs(x-y))
print(b)
