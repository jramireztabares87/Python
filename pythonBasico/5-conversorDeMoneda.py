pesos = float(input("¿Cuántos pesos colombianos tiene?: "))
valorDelDolar = 3956 #Valor a 06/02/2022
dolares = round((pesos / valorDelDolar),2) #Redondeando a dos decimales el resultado de la operación
print("Tienes $" + str(dolares) + " dolares")