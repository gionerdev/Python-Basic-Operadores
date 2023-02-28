# Operadores de comparación
# Estos op hacen comparativas con distintos datos y retorna valores booleanos

# Creando lista de operadores 


# Es igual que == evalua si los datos tienen el mismo contenido..
# Retorna True o False en caso contario. 

x = "Hello, Python" == 20
y = 5.5 == 30
z = "Hello, Google" == "Hello, Google"

# Es distinto que !=, evalua si el segundo segmento es distinto al primero.
# Retorna True si es distinto de otro modo sera False.

x = 15.0 != 10j
y = False != True
z = "IA" != "IA"

# Es mayor que >, evalua si el número es mayor.

a = 15 > 5 # True
b = 5 > 15 # False
c = 139 > 20 # True

# Es menor que <, evalua si un número es menor.

a = 5.8 < 4.5 # True
b = 4.5 < 3.3 # False
c = 5.5 < 8.9 # True 

# Es mayor o igual >=, evalua si un número es mayor o si es igual 

x = 45.0 >= 33.0 # True
y = 50.0 >= 50.0 # True
z = 60.0 >= 70.0 # False

# Es menor o igual que <=, evalua si un número es menor o igual

a = 100 <= 200 # True 
b = 200 <= 200 # True
c = 150 <= 50 # False


# is e is not hace una comparación exacta de dos objetos 
# Los datos para comparar tienen que estar contenidos en una variable

string = "Hello"
my_answer = "Hi!"

print(string is my_answer) # False
print(string is not my_answer) # True
