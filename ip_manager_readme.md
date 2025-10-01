# 🔐 IP Access Manager

Algoritmo em Python para gerenciamento automatizado de lista de permissões de endereços IP.

## 📋 Descrição

Este projeto tem como objetivo desenvolver um algoritmo em Python para gerenciar acessos restritos através do controle de endereços IP. Os endereços IP autorizados ficam armazenados no arquivo `allow_list.txt`, enquanto os que devem ser removidos estão definidos em uma lista `remove_list` dentro do código. O algoritmo verifica se há correspondências entre as listas e remove automaticamente os IPs da lista de permissões quando necessário.

## 🎯 Objetivos do Projeto

- Automatizar o gerenciamento de listas de controle de acesso
- Demonstrar manipulação de arquivos em Python
- Implementar lógica de verificação e remoção de elementos
- Garantir atualização segura de arquivos de configuração

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- Manipulação de arquivos (open, read, write)
- Estruturas de dados (listas, strings)
- Operações com strings (.split(), .join())

## 📁 Estrutura do Projeto

```
ip-access-manager/
│
├── README.md              # Documentação do projeto
├── ip_manager.py          # Código principal do algoritmo
└── allow_list.txt         # Arquivo de exemplo com IPs autorizados
```

## 🚀 Como Usar

### Pré-requisitos

- Python 3.x instalado

### Passos para Execução

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/fernando-acq/ip-access-manager.git
   cd ip-access-manager
   ```

2. **Prepare o arquivo de lista de permissões:**
   - Certifique-se de que o arquivo `allow_list.txt` existe no diretório
   - O arquivo deve conter endereços IP separados por espaços ou quebras de linha

3. **Configure a lista de remoção:**
   - Edite o arquivo `ip_manager.py`
   - Modifique a variável `remove_list` com os IPs que deseja remover

4. **Execute o script:**
   ```bash
   python ip_manager.py
   ```

5. **Verifique os resultados:**
   - O arquivo `allow_list.txt` será atualizado automaticamente
   - Os IPs da `remove_list` serão removidos da lista de permissões

## 💡 Funcionamento do Algoritmo

### Etapa 1: Abertura do Arquivo
Utiliza a palavra-chave `with` junto com a função `open()` para abrir o arquivo de forma segura, garantindo o fechamento automático.

### Etapa 2: Leitura do Conteúdo
O método `.read()` converte o conteúdo do arquivo em uma string para manipulação.

### Etapa 3: Conversão para Lista
O método `.split()` divide a string em uma lista de IPs individuais, facilitando a manipulação.

### Etapa 4: Iteração e Verificação
Um loop `for` percorre cada IP da lista, verificando se está presente na `remove_list`.

### Etapa 5: Remoção Condicional
Utiliza uma condicional `if` para garantir que apenas IPs presentes sejam removidos, evitando erros.

### Etapa 6: Atualização do Arquivo
Converte a lista de volta para string usando `.join("\n")` e grava no arquivo com `.write()`.

## 📊 Exemplo de Uso

**Conteúdo inicial de `allow_list.txt`:**
```
192.168.1.1
192.168.97.225
192.168.1.100
192.168.158.170
192.168.1.50
```

**Lista de remoção definida no código:**
```python
remove_list = ["192.168.97.225", "192.168.158.170"]
```

**Conteúdo final de `allow_list.txt` após execução:**
```
192.168.1.1
192.168.1.100
192.168.1.50
```

## 🔒 Segurança

O algoritmo garante:
- ✅ Fechamento automático de arquivos com `with`
- ✅ Verificação antes da remoção (evita erros)
- ✅ Preservação da integridade do arquivo original
- ✅ Atualização atômica do arquivo

## 📚 Conceitos Aplicados

- **Gerenciamento de contexto** (`with`)
- **Manipulação de arquivos** (leitura e escrita)
- **Estruturas de controle** (loops, condicionais)
- **Métodos de string** (.split(), .join())
- **Métodos de lista** (.remove())

## 🎓 Aprendizados

Este projeto demonstra competências essenciais em:
- Automação de tarefas administrativas
- Manipulação segura de arquivos
- Lógica de programação aplicada à segurança
- Boas práticas de desenvolvimento em Python

## 🤝 Contribuições

Sugestões e melhorias são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 👤 Autor

**Fernando Acquesta**
- GitHub: [@fernando-acq](https://github.com/fernando-acq)
- LinkedIn: [Fernando Acquesta](https://www.linkedin.com/in/fernando-acquesta-cybersecurity)

---

⭐ Se este projeto foi útil, considere dar uma estrela no repositório!