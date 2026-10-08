matriz = [
    [5, 8, 3],
    [2, 7, 9],
    [4, 6, 1]
]

quantidade = 0
for linha in matriz:
    for numero in linha:
        if numero % 2 == 0:
            print(numero)