def decoredor(func):#recibe como parametro una funcion
    def envoltura():#el contenido de esta nested function se asignara a una funcion recibida
        print("Esto se añade a mi funcion original")
        func()
    return envoltura #Retorna la nested function

@decoredor #Se adiciona syntactic sugar para que sea mas entendible, con esto la función saludo ya es modificada por la función decorador
def saludo():
    print("Hola!")
    
    
def run():
    saludo()
    
    # saludo2 = decoredor(saludo)
    # saludo2()


if __name__ == '__main__':
    run()    
    