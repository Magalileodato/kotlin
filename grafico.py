# Importa bibliotecas necessárias
import matplotlib.pyplot as plt  # Para gerar gráficos
import re  # Para usar expressões regulares e extrair os números
import os  # Para verificar diretórios, se necessário

# Função para ler um arquivo e extrair os valores de x e y
def ler_arquivo_pontos(nome_arquivo):
    x = []  # Lista para armazenar os valores de x
    y = []  # Lista para armazenar os valores de y
    try:
        # Abre o arquivo para leitura
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()[1:]  # Ignora a primeira linha (cabeçalho)
            for linha in linhas:
                # Usa regex para encontrar os números após x= e y=
                match = re.search(r'x=([-\d.Ee]+), y=([-\d.Ee]+)', linha)
                if match:
                    x.append(float(match.group(1)))  # Converte e adiciona o valor de x
                    y.append(float(match.group(2)))  # Converte e adiciona o valor de y
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
    return x, y  # Retorna as listas de x e y

# Define os nomes dos arquivos a serem lidos
arquivo_uniao = 'uniao.txt'
arquivo_inter = 'intercessao.txt'

# Chama a função para ler os arquivos e obter listas de x e y
x_u, y_u = ler_arquivo_pontos(arquivo_uniao)
x_i, y_i = ler_arquivo_pontos(arquivo_inter)

# Cria um vetor de tempo como índice dos pontos (0, 1, 2, ...)
tempo_u = list(range(len(x_u)))
tempo_i = list(range(len(x_i)))

# Gráfico 1: X vs Tempo (uniao.txt)
plt.figure(figsize=(10, 5))
plt.plot(tempo_u, x_u, label='Uniao - X', color='blue')
plt.title('Gráfico de X vs Tempo - uniao.txt')
plt.xlabel('Tempo')
plt.ylabel('Valor de X')
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico 2: Y vs Tempo (uniao.txt)
plt.figure(figsize=(10, 5))
plt.plot(tempo_u, y_u, label='Uniao - Y', color='green')
plt.title('Gráfico de Y vs Tempo - uniao.txt')
plt.xlabel('Tempo')
plt.ylabel('Valor de Y')
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico 3: X vs Tempo (intercessao.txt)
plt.figure(figsize=(10, 5))
plt.plot(tempo_i, x_i, label='Intercessao - X', color='red')
plt.title('Gráfico de X vs Tempo - intercessao.txt')
plt.xlabel('Tempo')
plt.ylabel('Valor de X')
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico 4: Y vs Tempo (intercessao.txt)
plt.figure(figsize=(10, 5))
plt.plot(tempo_i, y_i, label='Intercessao - Y', color='purple')
plt.title('Gráfico de Y vs Tempo - intercessao.txt')
plt.xlabel('Tempo')
plt.ylabel('Valor de Y')
plt.grid(True)
plt.tight_layout()
plt.show()
