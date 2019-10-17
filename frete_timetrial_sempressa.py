N, M = list(map(int, input().split()))
cidades = [[] for i in range(M - 1)]

for i in range(M):
    A, B, C = list(map(int, input().split()))
    A -= 1
    B -= 1
    cidades[A].append((B, C))
    cidades[B].append((A, C))

inicio = 0
fim = N - 1

custo = [float('inf') for i in range(M)]
custo[inicio] = 0
caminho = [(inicio, 0)]

while caminho != []:
    cid, preco = caminho.pop()
    for frt in cidades[cid]:
        if custo[frt[0]] > frt[1] + preco:
            custo[frt[0]] = frt[1] + preco
            caminho.append((frt[0], custo[frt[0]]))

print(custo[fim])