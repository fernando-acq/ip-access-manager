# Algoritmo para atualização de arquivos em Python
# Gerenciamento de acessos restritos via endereços IP

# Define o nome do arquivo que contém a lista de permissões
import_file = "allow_list.txt"

# Define a lista de endereços IP a serem removidos
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Abre o arquivo que contém a lista de permissões
with open(import_file, "r") as file:
    # Lê o conteúdo do arquivo e armazena em uma string
    ip_addresses = file.read()

# Converte a string em uma lista usando .split()
ip_addresses = ip_addresses.split()

# Percorre a lista de remoção
for element in ip_addresses:
    # Remove os endereços IP que estão na lista de remoção
    if element in remove_list:
        ip_addresses.remove(element)

# Converte a lista revisada novamente em uma string
ip_addresses = "\n".join(ip_addresses)

# Atualiza o arquivo com a lista revisada de endereços IP
with open(import_file, "w") as file:
    # Grava o conteúdo atualizado no arquivo
    file.write(ip_addresses)