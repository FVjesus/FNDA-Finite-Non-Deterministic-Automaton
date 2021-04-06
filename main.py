#Com a utilizacao de listas para armazenar o conjunto de estados foi possivel implementar o algoritmo de AFND
afd = {}
estados = input()
for i in estados.split(' '):
    afd[i] = {}
sigma = input()
indice = int(input())
for i in range(indice):
    x = input()
    x = x.split(' ')
    if(x[1]not in afd[x[0]]): 
        afd[x[0]][x[1]] = []    
    afd[x[0]][x[1]].append(x[2])
estadoI = input() 
estadoF = input()
F = {}
for i in estadoF.split(' '):
    F[i] = 'finalstate'
palavras = input()
for palavra in palavras.split(' '):
    e = []
    finalstat = 1
    for i in estadoI.split(' '):
        e.append(i)
    for char in palavra: 
        novoestado = []
        for e in e:
            if(afd[e].get(char)): 
                for i in range(len(afd[e][char])):
                    if(afd[e][char][i] not in novoestado):
                        novoestado.append(afd[e][char][i])
        e = novoestado
    for e in e:
        if(F.get(e)):
            finalstat = 0
    if(finalstat == 0):
        print('S')
    else:
        print('N')
