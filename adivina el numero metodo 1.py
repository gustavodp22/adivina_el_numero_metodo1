#metodo 1 adivina el numero
#!/usr/bin/python3
import random
n=random.randrange(1,100)
nu=int(input('Dime el número que crees que he elegido: '))
while nu!=n:
    if nu>n:
        nu=int(input('El número es mas pequeño'))
    elif nu<n:
        nu=int(input('El número es mas grande'))
print('Felicidades has adivinado que el número secreto es:',n)

