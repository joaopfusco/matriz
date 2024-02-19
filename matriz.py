import numpy as np
import math

def printMatriz(matriz):
    if isinstance(matriz, list):
        print(np.round(np.array(matriz), 2))
    else:
        print(matriz)

def prod_diagonal_principal(matriz):
    n = len(matriz)
    produto = 1
    for i in range(n):
        produto *= matriz[i][i]
    return produto

def valores_matriz_triangular(matriz):
    n = len(matriz)
    posicoes_matriz_triangular = []
    for i in range(n):
        for j in range(n):
            if i > j and matriz[i][j] != 0:
                posicoes_matriz_triangular.append((i, j))
    return posicoes_matriz_triangular

def determinante(matriz):
    matriz_triangularizada = gerar_matriz_triangularizada(matriz)
    return prod_diagonal_principal(matriz_triangularizada)

def cofator(matriz, linha, coluna):
    ordem = len(matriz)
    matriz_cofator = gerar_matriz(ordem - 1, complete=True)
    linha_cofator = 0
    coluna_cofator = 0
    for i in range(ordem):
        for j in range(ordem):
            if i != linha and j != coluna:
                matriz_cofator[linha_cofator][coluna_cofator] = matriz[i][j]

                coluna_cofator += 1
                if coluna_cofator == ordem:
                    linha_cofator += 1
                    coluna_cofator = 0
    
    det = determinante(matriz_cofator)
    cofator = det * ((-1)**(linha + coluna))
    return cofator

def gerar_matriz(ordem, complete=None):
    matriz = []
    c = 0
    for i in range(ordem):
        linha = []
        for j in range(ordem):
            if isinstance(complete, list):
                valor = complete[i][j]
            elif isinstance(complete, bool) and complete:
                c += 1
                valor = c
            else:
                valor = int(input(f"Valor ({i}, {j}): "))
                
            linha.append(valor)
        matriz.append(linha)
        
    return matriz

def gerar_matriz_triangularizada(matriz, printf=False):
    ordem = len(matriz)
    matriz_triangular = valores_matriz_triangular(matriz)
    matriz_triangularizada = gerar_matriz(ordem, complete=matriz)
    for p in matriz_triangular:
        linha_triangular, coluna_triangular = p
        valor_triangular = matriz_triangularizada[linha_triangular][coluna_triangular]

        linha = coluna_triangular
        coluna = coluna_triangular
        valor = matriz_triangularizada[linha][coluna]

        k = -1 * (valor_triangular / valor if valor != 0 else valor_triangular)

        for i in range(ordem):
            matriz_triangularizada[linha_triangular][i] += k * matriz_triangularizada[linha][i]

        if printf:
            print(f"L{linha_triangular + 1} -> L{linha_triangular + 1} + ({k:.2f}) * L{linha + 1}:")
            printMatriz(matriz_triangularizada)
            print()
        
    return matriz_triangularizada

def gerar_matriz_cofatores(matriz):
    ordem = len(matriz)
    matriz_cofatores = gerar_matriz(ordem, complete=True)
    for i in range(ordem):
        for j in range(ordem):
            matriz_cofatores[i][j] = cofator(matriz, i, j)
            
    return matriz_cofatores
            
def gerar_matriz_transposta(matriz):
    ordem = len(matriz)
    matriz_transposta = gerar_matriz(ordem, complete=True)
    for j in range(ordem):
        for i in range(ordem):
            matriz_transposta[j][i] = matriz[i][j]
        
    return matriz_transposta

def gerar_matriz_adjunta(matriz):
    matriz_cofatores = gerar_matriz_cofatores(matriz)
    matriz_adjunta = gerar_matriz_transposta(matriz_cofatores)

    return matriz_adjunta

def gerar_matriz_inversa(matriz):
    ordem = len(matriz)
    matriz_inversa = gerar_matriz_adjunta(matriz)
    det = determinante(matriz)
    
    if det == 0:
        return "Matriz não inversível."
    
    for i in range(ordem):
        for j in range(ordem):
            matriz_inversa[i][j] = matriz_inversa[i][j] * (1 / det)
    
    return matriz_inversa
