nombre = input("Ingrese una cadena: ")

print("\nTrae el caracter del indice 0: " + nombre[0])
print("Trae el caracter del indice 1: " + nombre[1])
print("Trae el caracter desde el indice 0 hasta el 3: " + nombre[0:3])
print("Trae el caracter desde el indice 3 hasta el final: " + nombre[3:])
print("Trae el caracter desde el indice 1 hasta el 7: " + nombre[1:7])
print("Trae el caracter desde el indice 1 hasta el 7 y de 2 en 2: " + nombre[1:7:2])
print("Trae la cadena completa: " + nombre[::])
print("Trae el caracter desde el indice 1 hasta el final y de 3 en 3: " + nombre[1::3])
print("Trae la cadena completa pero invertida: " + nombre[::-1])