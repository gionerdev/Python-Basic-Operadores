# Operadores Lógicos
# Estos op se utilizan para hacer operaciones lógicas 
# retorando valores discretos True o False

# Operador or (Equivalente a la suma)
# Si de dos segmentos uno es True, todos serán True

x = 0 # False
y = 0 # False
z = 1 # True

operación = (x > y)or(z >= y)

print(operación) # True


# Operador and (equivalente a la multiplicación)
# de dos casos si dos son True y uno es False, el resto sera false

a = 10
b = 20
c = 30

resultado = (a < b)and(b > c)

print(resultado)


# Operador not (equivalente a la resta)
# este operador invierte los valores True = False y False = True

m = 50
n = 40

operación = not (m > n) # False
operación_2 = not (m < n) # True

print(operación_2)


https://es.wikipedia.org/wiki/L%C3%B3gica_binaria
