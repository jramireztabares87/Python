nombre = input("Ingrese una cadena de texto: ")


print("\nPone en mayusculas la cadena de texto:  " + nombre.upper())
print("Pone en mayuscula la primer letra de la cadena: " + nombre.capitalize())
print("Elimina espacios al final de la cadena: " + nombre.strip())
print("Pone en minusculas la cadena de texto: " + nombre.lower())
print("Reemplaza caracteres en la cadena, en este caso la letra 'a' por el '#': " + nombre.replace('a','#'))
print("Muestra la longitud de la cadena: " + str(len(nombre)))
print("Muestra una pocsición especifica en la cadena, en esta caso la numero 3: "+ nombre[3])