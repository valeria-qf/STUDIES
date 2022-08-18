# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

ang = int(input('Digite o angulo: '))
sin = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))

print('Angulo {}: Sen={:.2f}, Cos={:.2f}, tg={:.2f}'.format(ang, sin, cos, tg))
