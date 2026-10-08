numeros = []

for i in range (8):
    num = int(input(f"Digite o {i + 1}))° número:"))
    numeros.append(num)

print("Números Pares:")

for num in numeros:
    if num % 2 ==0:
        print(num)