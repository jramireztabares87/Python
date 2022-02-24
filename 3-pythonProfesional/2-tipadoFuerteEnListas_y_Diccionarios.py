#Para trabajar con tipado de datos fuerte en estructuras de datos como listas, diccionarios y tuplas, se
# debe importar las clases Dict, List y Tuple del módulo typing

from typing import Dict, List, Tuple


# Para crear una lista de datos con tipado fuerte, se hace de forma similar a las variables:
# Se debe poner el nombre de la lista seguida por dos puntos “:” La clase List[ini] el carácter “=” seguido de los elementos que en este caso todos serán números
positives: List[int] = [1,2,3,4,5]


# Para crear un diccionario de datos con tipado fuerte, se hace de forma similar a las variables:
# Se debe poner el nombre del diccionario seguido por dos puntos “:” La clase Dict[tipo de dato del índice, tipo de datos del valor] el carácter “=” seguido de los elementos que en este caso las llaves serán string y los valores serán numéricos
users: Dict[str, int] = {
    'argentina': 1,
    'mexico': 34,
    'colombia': 45,
}


# Este caso es una lista la cual a su vez contiene un diccionario, cuyos índices y valores son de tipo string
countries: List[Dict[str, str]] = [
    {
        'name': 'Argentina',
        'people': '450000'
    },
    {
        'name': 'Mexico',
        'people': '9000000'
    },
    {
        'name': 'Colombia',
        'people': '999999999'
    },    
]

# Las tuplas al ser elementos inmutables, se puede declarar el tipo de datos para cada valor de esta, como lo
# muestra el ejemplo en donde el primer valor es entero, el segundo es float y el ultimo es entero 
numbers: Tuple[int, float, int] = (1, 0.5, 1)


# Todo lo explicado anteriormente se puede resumir o almacenar en una variable:
# Para este ejemplo la variable CoordinatesType almacena una lista que a su vez contiene un diccionario cuyos índices son
# de tipo string y los valores son una tupla con dos valores enteros
CoordinatesType = List[Dict[str, Tuple[int, int]]]

# De esta forma podemos declarar la estructura coordinates  de tipo CoordinatesType
coordinates: CoordinatesType = [
    {
        'coordi1': (1,2),
        'coordi2': (3,5),
    },
    {
        'coordi1': (0,1),
        'coordi2': (2,5),
    },    
]