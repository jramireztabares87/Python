from multiprocessing.sharedctypes import Value


def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firsname":"Johan", "lasname":"Ramirez"}
    
    #Una lista puede contener diccionarios como items
    super_list = [
        {"firsname":"Johan", "lasname":"Ramirez"},
        {"firsname":"Gabriel", "lasname":"Ramirez"},
        {"firsname":"Pedro", "lasname":"perez"},
        {"firsname":"Martin", "lasname":"Lopez"}
    ]
    
    
    #Un diccionario puede contener listas como valores de las llaves
    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,0],
        "floating_nums": [1.1, 4.5, 6.43]
    }
    
    
    #Ciclo para imprimir valores del super diccionario
    for key, Value in super_dict.items():
        print(key, "-", Value)
        
    
    #Ciclo para imprimir valores de la super lista
    for i in super_list:
        print(i)


if __name__ == '__main__':
    run()