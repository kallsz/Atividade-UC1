for aluno in range(1, 6):
    nota = float(input("Nota do Aluno: "))

    if nota >= 7:
        print("Aprovado")
    elif nota >= 5:
        print("Recuperação")
    else:
        print("Reprovado")