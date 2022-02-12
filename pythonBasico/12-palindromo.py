#Funcion para saber si una palabra es palindromo
def palindromo(palabra):
    palabra = palabra.replace(' ','').lower()
    if palabra == palabra[::-1]:
        return True
    else:
        return False
    
#Funcion principal    
def run():
    palabra = input("Escribe una palabra: ")
    esPalindromo = palindromo(palabra)
    if esPalindromo == True:
        print("Es palindromo! :)")
    else:
        print("No es palindromo :(")
        
#Punto de entrada en un programa de python, es un estandar
if __name__ == '__main__':
    run()