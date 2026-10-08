notas = []

for i in range(5):
    nota = float(input("Digite a nota:"))
    notas.append(nota)

media = sum(notas) / len(notas)

print("Notas:", notas)
print("Média:", media)
print("Maior Nota:", max(notas))
print("Menor Nota:", min(notas))
