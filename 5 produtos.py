produtos = []

for i in range(5):
    nome = input("Produtos: ")
    produtos.append(nome)

print("===Lista de Produtos===")

i = 0

while i < len(produtos):
    print(produtos[i])
    i += 1
