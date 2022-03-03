# Los generadores son una forma mas simple de implementar iteradores, no son más que syntactic sugar, en la
# cual se usa la key Word yield para guardar el ultimo valor de una variable en cada iteración del ciclo while
# import time

# def fibo_gen():
#     n1 = 0
#     n2 = 1
#     counter = 0
#     while True:
#         if counter == 0:
#             counter += 1
#             yield n1
#         elif counter == 1:
#             counter += 1
#             yield n2
#         else:
#             aux = n1 + n2
#             n1, n2 = n2, aux
#             counter +=1
#             yield aux
            
# def run():
#     fibonacci = fibo_gen()
#     for element in fibonacci:
#         print(element)
#         time.sleep(0.05)


# if __name__ == '__main__':
#     run()            
    
    
import time

def fibo_gen(max: int):
    n1 = 0
    n2 = 1
    counter = 0
    
    while counter <= max:        
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2            
        elif n1 <= max and n2 <= max:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter +=1
            yield aux
    
                    
def run():
    fibonacci = fibo_gen(10)
    for element in fibonacci:
        print(element)
        time.sleep(0.05)


if __name__ == '__main__':
    run()            
        