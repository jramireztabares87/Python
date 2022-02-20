#Algoritmo para saber los números divisores de un valor ingresado, en el cual se usa assert statements, adicional, se usa list comprehensions
def divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors


def run():
    num = input("Ingrese un número: ")
    assert num.isnumeric() and int(num) > 0, "No puedes ingresar caracteres diferentes a un número positivo"
    print(divisors(int(num)))
    print("Terminó mi programa")


if __name__ == '__main__':
    run()