'''
Javier Mombiela
Carne: 20067
Seccion: 21

Teoria de la Computacion
Proyecto 2: Funciones Lambda
'''

'''
Numeros
'''
cero = lambda f: lambda x: x
uno = lambda f: lambda x: f(x)
dos = lambda f: lambda x: f(f(x))
tres = lambda f: lambda x: f(f(f(x)))
cuatro = lambda f: lambda x: f(f(f(f(x))))

'''
Funciones
'''
sucesor = lambda n: lambda f: lambda x: f(n(f)(x))
suma = lambda a: lambda b: lambda f: lambda x: a(f)(b(f)(x))
multiplicacion = lambda a: lambda b: lambda f: lambda x: a(b(f))(x)
potencia = lambda a: lambda b: lambda f: lambda x: b(a)(f)(x)

alpha = lambda x: x + 1
beta = lambda x: 2 * x

'''
Ejemplos Alpha
'''
print("\n---------Alpha---------")
print("Sucesor de 0        : " + str(sucesor(cero)(alpha)(cero(alpha)(0))))
print("Suma(2,3)           : " + str(suma(dos)(tres)(alpha)(cero(alpha)(0))))
print("Multiplicacion(4,3) : " + str(multiplicacion(cuatro)(tres)(alpha)(cero(alpha)(0))))
print("Potencia(3,4)       : " + str(potencia(tres)(cuatro)(alpha)(cero(alpha)(0))))

'''
Ejemplos Beta
'''
print("\n---------Beta----------")
print("Sucesor de 0        : " + str(sucesor(cero)(beta)(cero(beta)(0.5))))
print("Suma(2,3)           : " + str(suma(dos)(tres)(beta)(cero(beta)(0.5))))
print("Multiplicacion(4,3) : " + str(multiplicacion(cuatro)(tres)(beta)(cero(beta)(0.5))))
print("Potencia(3,4)       : " + str(potencia(tres)(cuatro)(beta)(cero(beta)(0.5))))
