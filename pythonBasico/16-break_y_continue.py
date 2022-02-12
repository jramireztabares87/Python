def run():
    #Ejemplo de comousar continue, si la condición se cumple continua
    #de lo contrario salta esa iteración
    
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)
        
    #Ejemplo de Break
    #Si la variable iteradore i se encuentra con el valor 5678 el ciclo se rompe
    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break
    
    
    texto = input("Escribe un texto: ")
    for letra in texto:
        if letra == 'o':
            break
        print(letra)


if __name__ == '__main__':
    run()