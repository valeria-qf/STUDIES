# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar

R = float(input('How much money do you have? '))
print('You can buy {:.2f} dollars with {} reais'.format(R/5.21, R))
