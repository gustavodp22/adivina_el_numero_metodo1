#metodo 2 adivina el numero con un contador

import random
n=random.randrange(1,100)
nu=int(input('Dime el número que crees que he elegido '))
c=1
while nu!=n:
  c+=1
  if nu>n:
      nu=int(input('El número es mas pequeño'))
  elif nu<n:
      nu=int(input('El número es mas grande'))
print('Felicidades has adivinado que el número secreto es:',n)
print('Y lo has adivinado en',c,'intentos.')
