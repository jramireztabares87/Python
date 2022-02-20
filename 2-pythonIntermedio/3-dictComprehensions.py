def run ():
    # my_dict = {}
    
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         my_dict[i] = i**3
        
    # print(my_dict)
    
    
    # El anterior ejercicio se puede hace en una sola línea de código con el concepto de dictionary Comprenhensions estructurado de la siguiente forma:
    # Para cada iteración de i en un rango de 1 a 100, i se almacena como llave e i al cubo como valor, siempre y cuando i modulo de 3 sea diferente de 0

    # my_dict = {i:i**3 for i in range(1,101) if i % 3 != 0}        
    # print(my_dict)
    
    #-------------------------------------------------------------
    
    reto = {i:round(i**(0.5),2) for i in range(1, 1001)}
    print(reto)
    


if __name__ == '__main__':
    run()