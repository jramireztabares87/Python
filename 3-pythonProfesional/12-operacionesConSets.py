my_set1 = {1, 4, 5}
my_set2 = {5, 6, 7}


# La unión de los conjuntos o los sets se realiza con el carácter pipe | si existe un elemento repetido, este será eliminado 
my_set3 = my_set1 | my_set2
print("La unión es = ", my_set3)

# La intersección se realiza con el ampersand &, la intersección es seleccionar el elemento que se repite en ambos
my_set4 = my_set1 & my_set2
print("La intersección es = ", my_set4)

# La diferencia se realiza como una simple resta entre los sets
my_set5 = my_set1 - my_set2
print("Los elementos están en my_set1 y no estaán en my_set2 = ", my_set5)

my_set6 = my_set2 - my_set1
print("Los elementos están en my_set2 y no estaán en my_set1 = ", my_set6)

# La diferencia simetrica son aquellos elementos que NO se repiten en cada set
my_set7 = my_set2 ^ my_set1
print("La diferencia simetrica = ", my_set7)