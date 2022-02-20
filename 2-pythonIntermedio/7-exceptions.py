#Algoritmo para saber los números divisores de un valor ingresado, en el cual se usa las excepciones try y except

# def divisors(num):
#     divisors = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             divisors.append(i)
#     return divisors


# def run():
#     try:
#         num = int(input("Ingrese un número: "))
#         print(divisors(num))
#         print("Terminó mi programa")
        
#     except ValueError:
#         print("Debes ingresar un número")


# if __name__ == '__main__':
#     run()
    
    
#Algoritmo para saber los números divisores de un valor ingresado, en el cual se usa las excepciones try, raise y except, adicional, se usa list comprehensions
def divisors(num):
        

    try:
        if num <= 0:
            raise ValueError("No se pueden ingresar numeros negativos :(")
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        return divisors
    except ValueError as ve:
        print(ve)        


def run():
    try:
        num = int(input("Ingrese un número: "))
        print(divisors(num))
        print("Terminó mi programa")
        
    except ValueError:
        print("No debes ingresar caracteres distintos a un números positivos")


if __name__ == '__main__':
    run()