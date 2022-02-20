# Las lambdas funtions son funciones anónimas, no tienen nombre, no usan la key Word def, en vez de eso
# usan la key Word lambda seguida de los argumentos y luego la expresión 
palindromo = lambda string: string == string[::-1] 


def run():
    palabra = input("Ingrese una palabra: ")
    palabra = palabra.replace(' ','').lower()
    if palindromo(palabra):
        print("Es palindromo!")
    else:
        print("No es palindromo!")
    
    
if __name__ == '__main__':
    run()