DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    #La siguiente línea de código arroja los nombres de las personas que manejan Python como lenguaje usando list comprehension
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    #La siguiente línea de código arroja los nombres de las personas que manejan Python como lenguaje usando las funciones filter y map
    all_python_devs2 = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_devs2 = list(map(lambda worker: worker["name"], all_python_devs2))
    
    #La siguiente línea de código arroja los nombres de las personas que laboran en platzi list comprehension
    all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    #La siguiente línea de código arroja los nombres de las personas que laboran en platzi list comprehension usando las funciones filter y map
    all_Platzi_workers2 = list(filter(lambda worker: worker["organization"] == "Platzi",DATA))
    all_Platzi_workers2 = list(map(lambda worker: worker["name"] ,all_Platzi_workers2))

    #La siguiente línea de código arroja los nombres de las personas que son mayores de 18 años usando las funciones filter y map
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    #La siguiente línea de código arroja los nombres de las personas que son mayores de 18 años usando list comprehension
    adults2 = [worker["name"] for worker in DATA if worker["age"] > 18]
    
    #La siguiente línea de código arroja cada diccionario que esta dentro de la lista DATA y le adiciona la llave OLD usando la función map
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
    #La siguiente línea de código arroja cada diccionario que esta dentro de la lista DATA y le adiciona la llave OLD usando list comprehension
    old_people2 = [worker| {"old": worker["age"] > 70} for worker in DATA ]
    
    
     
    
    for worker in old_people2:
        print(worker)


if __name__ == '__main__':
    run()