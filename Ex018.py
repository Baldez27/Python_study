# import math
# ângulo = float(input('Digite o ângulo que você deseja: '))
# seno = math.sin(math.radians(ângulo))
# print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
# cosseno = math.cos(math.radians(ângulo))
# print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
# tangente = math.tan(math.radians(ângulo))
# print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(ângulo, tangente))

from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tangente))
