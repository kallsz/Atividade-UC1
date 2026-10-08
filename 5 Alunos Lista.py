alunos = []

for i in range(5):
    nome = input("Alunos: ")
    alunos.append(nome)

print("Alunos na Lista: ")
print(alunos)

# parte 2: Mostrar um aluno por linha.
i = 0

while i < len(alunos):
    print(alunos[i])
    i += 1
