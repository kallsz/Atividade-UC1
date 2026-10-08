matriz = [
    [7, 8, 9],
    [5, 6, 7],
    [8, 9, 10]
]

maior = matriz[0][0]

for linha in matriz:
    for numero in linha:
        if numero > maior:
            maior = numero