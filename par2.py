# Mostrar la suma de los primeros 30 numeros pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

suma_pares = 0
i = 0

while i < len(numeros):
    if numeros[i] % 2 == 0:
        suma_pares += numeros[i]
    i += 1

print('Suma de todos los valores pares que hay en el rango 1-30:', suma_pares)

print()