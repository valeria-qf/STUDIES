# working with modules
# import math
# from math import sqrt, ceil

import math

num = int(input('Enter a number: '))
root = math.sqrt(num)
# print(' the square root of {} is {}'.format(num, math.floor(root)))   # floor Arredonda para baixo e ceil para cima
print(' the square root of {} is {:.2f}'.format(num, root)) # 2 casas decimais
