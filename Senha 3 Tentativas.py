senha_correta = "python123"

for tentativa in range (3):
    senha = input("Digite a Senha: ")

    if senha == senha_correta:
          print("Acesso Permitido")
          break

    elif tentativa <=0:
        print("Senha Incorreta. Restam 2 Tentativas.")
    elif tentativa <=1:
        print("Senha Incorreta. Resta 1 Tentativa.")
    else:
        print("Senha Incorreta. Acesso Bloqueado.")
    





















   
    