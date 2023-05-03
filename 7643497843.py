import time, sqlite3, random
from random import randrange

tiempo=5
def tiempo():
    time.sleep(5)


equipo1 = input("Nombre de equipo 1: ")
equipo2 = input("Nombre de equipo 2: ")
respuesta=None 
print("\nBienvenido a Jumanji adventure")
print("\n Estas en el bosque con el equipo {} y con el equipo {}:\n".format(equipo1, equipo2))
print("\n\n Te encuentras con dos serpientes 1 es venenosa y otra no, pero no sabes cual no es venenosa\n")
print("La serpeinte numero 1 es verde con rayas rojas y la otra es roja con rayas verdes\n")
print("Tienen que adivinar cual no es venenosa")
input("Pon 1 para elegir a la serpiente 1 y 2 para la serpiente numero 2: ")

print(randrange(1,3))

if randrange(1,3) == 1:

    print("yeay")
