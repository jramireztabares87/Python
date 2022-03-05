# ELIMINAR ELEMENTOS DUPLICADOS DE UNA LISTA CON CILCOS FOR

# # Se crea una función que recibe la lista a la que se eliminaran los elementos duplicados
# def remove_duplicates(some_list):    
#     without_diplicates = [] #Se declara una lista vacia
#     for element in some_list: #La variable element recorre la lista que llega a la funcion
#         if element not in without_diplicates: #Si el valor de element no esta en la nueva lista, se ingresa, de lo contrario queda por fuera
#             without_diplicates.append(element)
#     return without_diplicates
    

# def run():
#     random_list = [1, 1, 2, 2, 4]
#     print(remove_duplicates(random_list))


# if __name__ == '__main__':
#     run()   
    
#--------------------------------------------------------------------------------------------------------------------
# ELIMINAR ELEMENTOS DUPLICADOS DE UNA LISTA CON SET

# Se crea una función que recibe la lista a la que se eliminaran los elementos duplicados
def remove_duplicates(some_list):        
    return list(set(some_list))
    

def run():
    random_list = [1, 1, 2, 2, 4]
    print(remove_duplicates(random_list))


if __name__ == '__main__':
    run()    