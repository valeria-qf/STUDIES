# coding=utf-8
# Faça um programa que leia o comprimento do cateto oposto e do cat adj de um tri retangulo.  Calcule e mostre o
# comprimento da hipotenusa

import math

catop = float(input('Digite o valor do cat oposto : '))
catadj = float(input('Digite o valor do cat adjacente : '))
hip = math.hypot(catop, catadj)
print('O comprimento da hipotenusa é {:.2f}'.format(hip))
