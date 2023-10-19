# Lista para armazenar os dados dos usuários
usuarios = []

# Solicita ao usuário os dados e armazena na lista
while True:
    nome = input("Digite o nome do usuario (ou deixe em branco para sair): ")
    if nome == "":
        break
    espaco = int(input("Digite o espaco utilizado pelo usuario em bytes: "))
    usuarios.append((nome, espaco))

# Cria o arquivo "usuarios.txt" e escreve os dados
with open("usuarios.txt", "w") as file:
    for nome, espaco in usuarios:
        file.write(f"{nome:<15} {espaco}\n")

print("Arquivo 'usuarios.txt' gerado com sucesso.")
