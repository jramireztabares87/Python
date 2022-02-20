def run():
    
    # squares = [] #Se crea una lista vacia
    # #La variable i recorre el ciclo de 1 a 100
    # for i in range(1, 101):
    #     #Si cada posicion de de i modulo de 3 es diferente de 0, entonces se agrega a la lista squares el cuadrado de cada posicion de i
    #     if i % 3 != 0:
    #         squares.append(i**2)
    # #Se imprime la lista                    
    # print(squares)
    
    # El anterior ejercicio se puede hace en una sola línea de código con el concepto de list Comprenhensions estructurado de la siguiente forma:
    # Para cada posición de i al cuadrado iterarla en un rango de 1 a 100 siempre y cuando se cumpla la condición de que el modulo de 3 sea diferente de 0

    # squares = [i**2 for i in range(1,101) if i % 3 != 0]
    # print(squares)


    #Numero hasta el 10.000 que son multiplos de 4, 6 y 9 al mismo tiempo
    multiplos = [i for i in range (1, 10001) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(multiplos)
    

if __name__ == '__main__':
    run()
    