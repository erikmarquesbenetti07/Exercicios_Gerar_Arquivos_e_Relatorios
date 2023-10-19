import random

# Função para gerar endereços IP válidos
def generate_valid_ip():
    ip_parts = [str(random.randint(0, 255)) for _ in range(4)]
    return '.'.join(ip_parts)

# Função para gerar endereços IP inválidos
def generate_invalid_ip():
    ip_parts = [str(random.randint(256, 999)) for _ in range(4)]
    return '.'.join(ip_parts)

# Gerar uma lista de endereços IP válidos e inválidos
num_valid_ips = 5
num_invalid_ips = 5
addresses = [generate_valid_ip() for _ in range(num_valid_ips)] + [generate_invalid_ip() for _ in range(num_invalid_ips)]

# Embaralhar a lista de endereços
random.shuffle(addresses)

# Escrever a lista de endereços em um arquivo
with open('enderecos.txt', 'w') as file:
    for address in addresses:
        file.write(address + '\n')

print(f'Arquivo "enderecos.txt" gerado com {num_valid_ips} endereços IP válidos e {num_invalid_ips} endereços IP inválidos.')
