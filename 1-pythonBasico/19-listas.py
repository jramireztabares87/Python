objetos = [1,2,3,4,5,6,7,8,9,] #una lista puede almacenar varios valores
print(objetos)
variosObjetos =["hola",3,5.8,6,True]#Una lista tambien puede contener valores de diferentes tipos de datos
print(variosObjetos)

#Recorrer la lista con un for
for i in variosObjetos:
    print(i)

print(variosObjetos[2])# se puede imprimir un solo objeto por medio de su indice

variosObjetos.append(False) #Con el metodo append se inserta un elemento al final
print(variosObjetos)

variosObjetos.pop(2)#Con el metodo pop se elimina un elemento por medio del su indice
print(variosObjetos)

