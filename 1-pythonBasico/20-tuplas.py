# Las tuplas tienen estructuras similares a las litas, estas poseen índices y se imprimen de igual forma 
# pero su gran diferencia es que sus datos no pueden cambiar, no se pueden adicionar o eliminar elementos
# es decir que son inmutables al igual que los string

miTupla = (1,2,3,4,5,6,"hola")

print(miTupla[0])
print(miTupla)

for i in miTupla:
    print(i)