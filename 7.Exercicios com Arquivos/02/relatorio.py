# Função para converter bytes em megabytes
def bytes_to_mb(bytes):
    return bytes / (1024 * 1024)

# Função para calcular o percentual de uso
def calculate_percentage(used_space, total_space):
    return (used_space / total_space) * 100

# Lê o arquivo "usuarios.txt" e armazena os dados em uma lista
users_data = []
with open("usuarios.txt", "r") as file:
    for line in file:
        name, used_space = line.strip().split()
        used_space = int(used_space)
        users_data.append((name, used_space))

# Calcula o espaço total ocupado e encontra o maior valor
total_space = sum(used_space for name, used_space in users_data)
max_space = max(used_space for name, used_space in users_data)

# Cria o relatório "relatório.txt"
with open("relatorio.txt", "w") as report_file:
    report_file.write("ACME Inc.               Uso do espaco em disco pelos usuarios\n")
    report_file.write("-" * 70 + "\n")
    report_file.write("Nr.  Usuario        Espaco utilizado     % do uso\n")

    for i, (name, used_space) in enumerate(users_data, start=1):
        mb_used_space = bytes_to_mb(used_space)
        percentage = calculate_percentage(used_space, total_space)
        report_file.write(f"{i:<4} {name:<15} {mb_used_space:>10.2f} MB {percentage:>17.2f}%\n")

    report_file.write(f"\nEspaco total ocupado: {bytes_to_mb(total_space):.2f} MB\n")
    report_file.write(f"Espaco medio ocupado: {bytes_to_mb(total_space / len(users_data)):.2f} MB\n")

print("Relatorio gerado com sucesso.")
