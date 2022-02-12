import random

def generar_contrasena(cantidad_caracteres):
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    simbolos = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    numeros = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    
    caracteres = mayusculas + minusculas + simbolos + numeros
    
    contrasena = []
    
    for i in range(cantidad_caracteres):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
        
    contrasena = "".join(contrasena)
    return contrasena
    
    
def run():
    cantidad_caracteres = int(input("¿Cuantos caracteres desea generar? "))
    contrasena = generar_contrasena(cantidad_caracteres)
    print("Tu nueva contraseña es: " + contrasena)


if __name__ == '__main__':
    run()