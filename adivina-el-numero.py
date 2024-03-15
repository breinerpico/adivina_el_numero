# input

from random import *

numero_secreto= randint(1,30)

intento=int(input("digite un numero del 1 al 30: "))

if intento<numero_secreto:
    print("el numero es mayor")

elif intento>numero_secreto:
    print("el numero es menor")

else:
    print("Felicidades, el numero e correcto")
    