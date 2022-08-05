# Faça um programa que leia a largura e a altura de uma parece em metros, calcule a sua area e a quantidade e tinta
# necessaria para pinta-la sabendo que a cada litro de tinta pinta uma area de 2m²

H = float(input('Enter the height: '))
L = float(input('Enter the width: '))
A = H*L
print('The amount of paint needed is {:.2f}L'.format(A/2))

