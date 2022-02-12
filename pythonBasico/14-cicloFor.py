#Ciclo que imprime una serie de numeros del 1 hasta el 1000
"""
for contador in range(1, 1001):
    print(contador)
    
"""    
    
#ciclo que imprime los resultados de la tabla del 11
"""
for i in range(10):
    print(11 * i)

"""


def run():
    tabla = int(input("Que tabla desea ingresar? "))
    
    for contador in range(0, 11):
        print(str(tabla) + "x" + str(contador) + "=" + str(tabla * contador))


if __name__ == '__main__':
    run()