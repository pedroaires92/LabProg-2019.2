#                              # # # MAPA # # #                               #

# O reino de Retônia é dividido em oito províncias, como mostradas na matriz abaixo. Qual o
# número mínimo de cores que são necessárias para colorir cada província com uma cor diferente, de
# modo que duas províncias vizinhas não tenham a mesma cor?

#  #  #  #  #  #  #  #  #  #  #  IMPLEMENTAÇÃO  #  #  #  #  #  #  #  #  #  #  #

# O algoritmo consiste em começar tentando colorir a região (representada por uma matriz) com uma configuração de
# N cores, e caso detectar que não seja possível, tentar com N+1. Repete isso até encontrar uma solução ou atingir
# o limite de tentativas válidas.

def tente_colorir(grafo, num_cores):                                   # Função que tenta construir uma configuração de
    assert num_cores >= 0, 'Número de cores inválido: %s' % num_cores  # cores para um grafo. Caso encontre uma
    cores = {}                                                         # configuração de cor válida a função a devolve
    def adjacentes_tem_cores_diferentes(nos, cor):                     # como um dicionário.Caso contrário,devolve None
        return all(cor != cores.get(n) for n in nos)
    for no, adjacentes in grafo.items():
        cor_achada = False
        for cor in range(num_cores):
            if adjacentes_tem_cores_diferentes(adjacentes, cor):
                cor_achada = True
                cores[no] = cor
                break
        if not cor_achada:
            return None
    return cores

def achar_cores_grafo(grafo):                          # Função que aplica a função tente_colorir() com diferentes
    for num_cores in range(1, len(grafo)):             # valores para o numero de cores. Dando assim, uma solução geral.
        cores = tente_colorir(grafo, num_cores)
        if cores:
            return cores

# Questão 3: Não é possível colorir com menos de 3 cores, pois existem 3 regiões com fronteiras entre si. Então,
#            tentaremos colorir com 3:

mapa = {'A': ['B', 'E'],
        'B': ['A', 'E', 'F', 'G', 'C'],
        'C': ['B', 'G', 'H', 'D'],
        'D': ['C', 'H'],
        'E': ['A', 'B', 'F', 'H'],
        'F': ['B', 'G', 'H', 'E'],
        'G': ['B', 'C', 'H', 'F'],
        'H': ['E', 'F', 'G', 'C', 'D'],
        }
tente_colorir(mapa, 3)

>>> {'A': 0, 'C': 0, 'F': 0, 'B': 1, 'H': 1, 'D': 2, 'E': 2, 'G': 2}