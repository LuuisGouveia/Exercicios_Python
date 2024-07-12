# adquirindo o numero da ordem da matriz
m = int(input("Qual a ordem da matriz?: "))
# duplicando o numero para ter uma matriz quadrada
n = m

# criação da matriz principal na memoria
mat = [[0 for x in range(n)] for x in range(m)]
# criação da matriz que será alterada na memoria
alterada = [[0 for x in range(n)] for x in range(m)]

# interando sobre a matriz principal
for i in range(m):
    for j in range(n):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

# realizando a soma dos positivos
soma = 0
for i in range(m):
    for j in range(n):
       if mat[i][j] >= 0:
        soma = soma + mat[i][j]

# saida da soma dos positivos
print(f"Soma dos positivos: {soma}")

# escolha de linhas da matriz e exibição da mesma
linha = int(input("Escolha uma linha: "))
print("Linha Escolhida: ", end=" ")
for i in range(n):
   print(mat[linha][i], end=" ")

# pulando linha
print()

# escolha da coluna da matriz e exibição da mesma
coluna = int(input("Escolha uma coluna: "))
print("Coluna Escolhida: ", end=" ")
for i in range(m):
   print(mat[i][coluna], end=" ")

# pulando linha
print()

# exibindo a diagonal principal da matriz
print("Diagonal Principal: ", end=" ")
for i in range(m):
    print(mat[i][i])

# aplicando a alteração da matriz, negativos elevados ao quadrado
for i in range(m):
    for j in range(n):
        if mat[i][j] < 0:
            alterada[i][j] = mat[i][j] ** 2
        else:
            alterada[i][j] = mat[i][j]

# exibindo a matriz alterada
print("Matriz Alterada: ")
for i in range(m):
    for j in range(n):
        print(f"{alterada[i][j]}", end="  ")
    print()


