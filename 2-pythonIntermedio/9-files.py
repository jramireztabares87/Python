# Significado del segundo parametro del metodo open
# r = lectura
# w = escritura y sobre escritura
# a = adiciona el contenido sin borrar el existente

def read():
    numbers = []
    with open ("./archivos/numbers.txt","r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)
    
        
def write():
    names = ["Johan","Gabriel","Nícol","Jennifer","Martín"]
    with open("./archivos/names.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def run():
    #read()
    write()


if __name__ == '__main__':
    run()