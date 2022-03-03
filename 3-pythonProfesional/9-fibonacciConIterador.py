#Un iterador Es una estructura de datos para guardar datos de manera infinita
#en este ejemplo se guar la secuencia fobonacci completa
# import time


# class FiboIter():
    
#     def __iter__(self):
#         self.n1 = 0
#         self.n2 = 1
#         self.counter = 0
#         return self
    
    
#     def __next__(self):
#         if self.counter == 0:
#             self.counter += 1
#             return self.n1
#         elif self.counter == 1:
#             self.counter += 1
#             return self.n2
#         else:
#             self.aux = self.n1 + self.n2
#             # self.n1 = self.n2
#             # self.n2 = self.aux
#             #Las dos lineas anteriores se pueden resumir de la siguiente manera
#             self.n1, self.n2 = self.n2, self.aux
#             self.counter += 1
#             return self.aux
            

# if __name__ == '__main__':
#     fibonacci = FiboIter()
#     for element in fibonacci:
#         print(element)
#         time.sleep(0.05)



#En este ejemplo se guarda la secuencia fibonacci pero con un limite dado por el usuario
import time

class FiboIter():
    
    def __init__ (self, max=None):
        self.max = max
        
    
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self
    
    
    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        elif not self.counter or (self.n1 <= self.max and self.n2 <= self.max):
            self.aux = self.n1 + self.n2
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux        
        else:
            raise StopIteration


def run():
    limite = int(input("Hasta donde desea imprimir la secuencia Fibonacci? "))
    fibonacci = FiboIter(limite)
    
    for element in fibonacci:
        print(element)
        time.sleep(0.05)


if __name__ == '__main__':
    run()            