matriz = [
    [5, 8, 3],
    [2, 7, 9],
    [4, 6, 1]
]


maior = matriz [0][0]

for linha in matriz:
    for numero in linha:
        if numero > maior:
            maior = numero