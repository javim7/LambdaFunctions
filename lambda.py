'''
Javier Mombiela
Carne: 20067
Seccion: 21

Teoria de la Computacion
Proyecto 2: Funciones Lambda
'''

print((lambda x: x+1)(10))
def high(x, func): return x + func(x)


print(high(2, lambda x: x*x))
