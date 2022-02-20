import random

def run():
    numero_aleatorio = random.randint(1,100)
    numero_elegido = int(input("Elige un numero del 1 al 100: "))
    
    contador = 1 #Contador iniciado en 1 para que cuente el primer intento que esta afuera del ciclo
    
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Busca un número mas grande")
        else:
            print("Busca un número mas pequeño")
        numero_elegido = int(input("Elige otro número: "))
        contador += 1 #Se cuenta cada intento
    print("¡Ganaste! " + str(contador) + " intentos") #Se imprimen los intentos


if __name__ == '__main__':
    run()