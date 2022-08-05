# Arithmetic operators
# + ADDITION, - SUBTRACTION, * MULTIPLICATION, / DIVISION
# ** POWER, // INT DIVISION, % REMAINDER OF DIVISION

n1 = int(input('Enter a value: '))
n2 = int(input('Enter another value: '))
s = n1+n2
m = n1*n2
d = n1/n2
dint = n1//n2
p = n1**n2

print('sum is {}, \n multiplication is {}, division is {:.3f} '.format(s, m, d), end=' ')
print('Int division is {}, pow is {}'.format(dint, p))

# {:.3} ==> mostrar 3 casas decimais / show 3 decimal places
# end=' ' ==> Não quebrar a linha/don't break the line
# \n ==> Breaks the line
print('Int division is {}, pow is {}'.format(dint, p))

