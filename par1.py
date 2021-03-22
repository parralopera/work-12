# Mostrar los primeros 10 numeros negativos impares
numeros = [0,-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

suma_negativa = 0
i = 0

while i < len(numeros):
    if numeros[i] % -2 != 0:
        suma_negativa += numeros[i]
    i += 1

print('Suma de todos los valores impares negativos que hay en el rango 1-10:', suma_negativa)