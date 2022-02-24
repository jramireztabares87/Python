# Para declarar el tipo de una variable se coloca el nombre de la variable seguido por dos puntos y el tipo

a: int = 5
print(a)

b: str = "Hola"
print(b)

c: bool = True
print(c)

# Para declararlo dentro de una función debe ser igual, adicional, si el retorno
# de la función debe ser de algún tipo especifico, se declara con '->' seguido del tipo de dato
def suma(a: int, b: int) -> int:
    return a + b

print(suma(1, 2))