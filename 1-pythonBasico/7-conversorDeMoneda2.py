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
    pesos = float(input("¿Cuántos pesos colombianos tiene?: "))
    valorDelDolar = 3956 #Valor a 06/02/2022
    dolares = round((pesos / valorDelDolar),2) #Redondeando a dos decimales el resultado de la operación
    print("Tienes $" + str(dolares) + " dolares")
    
elif opcion == 2:
    pesos = float(input("¿Cuántos pesos Argentinos tiene?: "))
    valorDelDolar = 105 #Valor a 06/02/2022
    dolares = round((pesos / valorDelDolar),2) #Redondeando a dos decimales el resultado de la operación
    print("Tienes $" + str(dolares) + " dolares")
    
elif opcion == 3:
    pesos = float(input("¿Cuántos pesos Mexicanos tiene?: "))
    valorDelDolar = 20 #Valor a 06/02/2022
    dolares = round((pesos / valorDelDolar),2) #Redondeando a dos decimales el resultado de la operación
    print("Tienes $" + str(dolares) + " dolares")
    
else:
    print("Por favor elija una opción")