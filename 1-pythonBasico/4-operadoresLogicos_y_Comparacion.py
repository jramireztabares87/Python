esEstudiante = True
esEmpleado = False
numeroUno = 10
numeroDos = 5

#Cuando en dos variables ambas deben ser verdaderas se debe usar el operador and
print ("Es estudiante y empleado al mismo tiempo: " + str(esEstudiante and esEmpleado))

#Cuando en dos variables solo una debe ser verdadera se debe usar el operador or
print ("Es estudiante o empleado : " + str(esEstudiante or esEmpleado))

#Cuando dos variables deben ser igualadas o comparadas se debe usar ==
print("El numero 1 es igual al numero 2: " + str(numeroUno == numeroDos))

#Cuando dos variables deben ser diferentes se debe usar !=
print("El numero 1 es diferente al numero 2: " + str(numeroUno != numeroDos))

#Operadores Logicos
print("El numero 1 es mayor al numero 2: " + str(numeroUno > numeroDos))
print("El numero 1 es menor al numero 2: " + str(numeroUno < numeroDos))
print("El numero 1 es mayor o igual al numero 2: " + str(numeroUno >= numeroDos))
print("El numero 1 es menor o igual al numero 2: " + str(numeroUno <= numeroDos))