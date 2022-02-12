def conversor(tipoPeso, valorDelDolar):
    pesos = float(input("¿Cuántos pesos " + tipoPeso +" tiene?: "))    
    dolares = round((pesos / valorDelDolar),2) #Redondeando a dos decimales el resultado de la operación
    print("Tienes $" + str(dolares) + " dolares")    


#Cuando se usan las commilas triples en python, este tiene encuenta los saltos de linea
menu = """
        Bienvenido al conversor de moneda

        1 - Pesos Colombianos
        2 - Pesos Argentinos
        3 - Pesos Mexicanos

        Elige una opcion:
        """
opcion = int(input(menu))

if opcion == 1:
    conversor("Colombianos", 3956) #Valor del dollar a 06/02/2022
elif opcion == 2:
    conversor("Argentinos", 105) #Valor del dollar a 06/02/2022
elif opcion == 3:
    conversor("Mexicanos", 20) #Valor del dollar a 06/02/2022
else:
    print("Por favor elija una opción")