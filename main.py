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
cero   = lambda f: lambda x: x
uno    = lambda f: lambda x: f(x)
dos    = lambda f: lambda x: f(f(x))
tres   = lambda f: lambda x: f(f(f(x)))
cuatro = lambda f: lambda x: f(f(f(f(x))))

'''
Funciones
'''
sucesor        = lambda n: lambda f: lambda x: f(n(f)(x))
suma           = lambda a: lambda b: lambda f: lambda x: a(f)(b(f)(x))
multiplicacion = lambda a: lambda b: lambda f: lambda x: a(b(f))(x)
potencia       = lambda a: lambda b: lambda f: lambda x: b(a)(f)(x)

alpha = lambda x: x + 1
beta  = lambda x: 2* x

'''
Ejemplos Alpha
'''
print("\n---------Alpha---------")
print("Sucesor de 0        : " + str(sucesor(cero)(alpha)(0)))
print("Suma(2,3)           : " + str(suma(dos)(tres)(alpha)(0)))
print("Multiplicacion(4,3) : " + str(multiplicacion(dos)(tres)(alpha)(0)))
print("Potencia(3,4)       : " + str(potencia(tres)(cuatro)(alpha)(0)))


'''
Ejemplos Beta
'''
print("\n---------Beta----------")
print("Sucesor de 0        : " + str(sucesor(cero)(beta)(0)))
print("Suma(2,3)           : " + str(suma(dos)(tres)(beta)(0)))
print("Multiplicacion(4,3) : " + str(multiplicacion(dos)(tres)(beta)(0)))
print("Potencia(3,4)       : " + str(potencia(tres)(cuatro)(beta)(0)))


'''
Explicacion
'''
print("\n------Explicacion------")
print("A la hora de utilizar las funciones Alpha y Beta, podemos observar que la diferencia es que alpha si despliega los resultados esperados, mientras que beta solo despliega cero para todo. Por lo tanto, podemos concluir que los resultados esperados con las funciones definidas, se obtienen con Alpha y con el parametro 0.")