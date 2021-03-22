# Serie Fibonacci
def naci(n):
    primer_numero, siguiente_numero = 0,1
    while primer_numero < n:
        print(primer_numero, end=' ')
        primer_numero, siguiente_numero = siguiente_numero, primer_numero+siguiente_numero
    print()
naci(100)