# Un closure debe de cumplir 3 condiciones para ser considerado como tal:
# 1 – debe tener una nested function o función anidada
# 2 – la nested function debe de hacer uso de una variable superior
# 3 – se debe de retornar la nested function

def make_repeater_of(n):
    # Condición 1
    def repeater(string):
        assert type(string) == str, "Solo puedes utilizar cadenas"
        return string * n #Condición 2
    return repeater #Condición 3
    
    
def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Hola"))
    
    repeat_10 = make_repeater_of(10)
    print(repeat_10("Johan"))


if __name__ == '__main__':
    run()