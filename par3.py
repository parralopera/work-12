# Mostrar la suma de los primeros 10 numeros impares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

suma_impares = 0
i = 0

while i < len(numeros):
    if numeros[i] % 2 != 0:
        suma_impares += numeros[i]
    i += 1

print('Suma de todos los valores impares que hay en el rango 1-10:', suma_impares)

print()