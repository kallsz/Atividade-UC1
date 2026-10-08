nome = input("Nome: ")
idade = int(input("Idade: "))
altura = float(input("Altura: "))

estudando = input("Você estuda programação? (sim/não): ")

estudando = estudando.lower() == "sim"

print("Informações")
print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("Estudando programação:", estudando)