# Função para verificar se um endereço IP é válido
def is_valid_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True

# Ler o arquivo de entrada
with open('enderecos.txt', 'r') as file:
    lines = file.readlines()

valid_ips = []
invalid_ips = []

# Verificar cada endereço IP e classificá-los como válidos ou inválidos
for line in lines:
    ip = line.strip()
    if is_valid_ip(ip):
        valid_ips.append(ip)
    else:
        invalid_ips.append(ip)

# Escrever o relatório no arquivo de saída
with open('relatorio.txt', 'w') as file:
    file.write('[Enderecos validos:]\n')
    for valid_ip in valid_ips:
        file.write(valid_ip + '\n')
    
    file.write('\n[Enderecos invalidos:]\n')
    for invalid_ip in invalid_ips:
        file.write(invalid_ip + '\n')

print('Relatorio gerado com sucesso!')
