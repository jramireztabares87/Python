from datetime import datetime

def execution_time(func):#Función decoradora
    def wrapper(*args, **kwargs): #La nested function indicando que funciona con o sin parametros definidos de la forma *args y **kwargs
        initial_time = datetime.now() #Hora hactual
        func(*args, **kwargs)
        final_time = datetime.now() #Hora final
        time_elapsed = final_time - initial_time #Segundos entre la hora final y la actual
        print("Pasaron " + str(time_elapsed.total_seconds()) + " Segundos")
    return wrapper #Retorno de la nested function


@execution_time
def random_func():
    for _ in range (1, 10000000):
        pass
  
  
@execution_time
def suma(a: int, b: int) -> int:
    return a + b
  
@execution_time
def saludo(nombre = "Johan"):
    print("Hola " + nombre)
    

def run():
    random_func()
    suma(20,7)
    saludo()   


if __name__ == '__main__':
    run()