import random;
import concurrent.futures;

# Função de complexidade constante O(1)
def gerar_numeros():
    torcedores = (random.randint(0, 1000))
    torcedores_casa = (random.randint(0, torcedores))
    torcedores_rival = torcedores - torcedores_casa

    return torcedores, torcedores_casa, torcedores_rival

# Função de complexidade constante O(1)
def criar_catraca ():
    a, b, c = gerar_numeros()
    catraca = [a, b, c]

    return catraca

# Função de complexidade constante O(1)
def gerar_numeros_threads(num_threads):
    catracas = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        for _ in range(num_threads):
            future = executor.submit(criar_catraca)
            catracas.append(future.result())
    return catracas

# Função de complexidade linear O(N)
def calcular_total (lista):
    total_torcedores = 0
    total_casa = 0
    total_visitante = 0

    for item in lista:
        total_torcedores = total_torcedores + item[0]
        total_casa = total_casa + item[1]
        total_visitante = total_visitante + item[2]

    return total_torcedores, total_casa, total_visitante

# Função de complexidade constante O(1)
def imprimir_total(total_torcedores, total_casa, total_visitante):
    print(f"Total de torcedores: {total_torcedores}")
    print(f"Total de torcedores do time da casa: {total_casa}")
    print(f"Total de torcedores do time de fora: {total_visitante}")

# Função de complexidade linear O(N)
def imprimir_catraca (lista):
    
    for item in lista:
        print(f"Catraca {lista.index(item) + 1}")
        print(f"Torcedores: {item[0]}")
        print(f"Torcedores do time da casa: {item[1]}")
        print(f"Torcedores do time de fora: {item[2]}")

# Função de complexidade quadrática O(N^2)
def organizar_ordem(lista):
    n = len(lista)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    
    return lista

# Função de complexidade linear O(N)
def imprimir_ordem_crescente(lista):
    lista_torcedores_catraca = []
    lista_torcedores_casa = []
    lista_torcedores_visitante = []

    for item in lista:
        lista_torcedores_catraca.append(item[0])
        lista_torcedores_casa.append(item[1])
        lista_torcedores_visitante.append(item[2])
    
    print("Ordem crescente do total de torcedores por catraca: ")
    print(organizar_ordem(lista_torcedores_catraca))
    print("Ordem crescente do total de torcedores do time da casa por catraca: ")
    print(organizar_ordem(lista_torcedores_casa))
    print("Ordem crescente do total de torcedores do time visitante por catraca: ")
    print(organizar_ordem(lista_torcedores_visitante))

# Função de complexidade exponencial O(2^N)
def gerar_conjuntos_torcedores_casa(lista):
    combinacoes = []
    
    n = len(lista)
    for i in range(2**n):
        combinacao = []
        for j in range(n):
            if i & (1 << j):
                combinacao.append(lista[j][1])
            else:
                combinacao.append("")
        combinacoes.append(combinacao)
    
    print(combinacoes)

if __name__ == '__main__':
    lista_geral = gerar_numeros_threads(10)
    
    total_torcedores, total_casa, total_visitante = calcular_total(lista_geral)
    imprimir_total(total_torcedores, total_casa, total_visitante)
    imprimir_catraca(lista_geral)
    imprimir_ordem_crescente(lista_geral)
    gerar_conjuntos_torcedores_casa(lista_geral)