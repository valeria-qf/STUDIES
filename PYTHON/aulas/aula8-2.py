# Create a program that reads any real number and print their int portion

import math

num = float(input('Enter a number: '))
num2 = math.trunc(num)
print('the int part of {} is {}'.format(num, num2))


