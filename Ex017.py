# co = float(input('Digite o valor do cateto oposto: '))
# ca = float(input('Digite o valor do cateto adjacente: '))
# hipot = (co ** 2 + ca ** 2) ** (1/2)
# print('A hipotenusa vai medir {:.2f}'.format(hipot))

from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hipot = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hipot))
