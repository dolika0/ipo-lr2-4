#вариант 4
import math
x=int(input("Введите x: "))
y=int(input("Введите y: "))
z=int(input("Введите z: "))
#n=x**(1/3)
#p=x**(y+2)
#m=abs(x-y)
#s=(math.asin(z))**2
#b=(10*(n+p))**(1/2)*(s-m)
b=((10*((x**(1/3))+(x**(y+2))))**(1/2))*((math.asin(z))**2-abs(x-y))
print(b)