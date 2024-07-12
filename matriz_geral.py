m = int(input("Qual a ordem da matriz?: "))
n = m

mat = [[0 for x in range(n)] for x in range(m)]
alterada = [[0 for x in range(n)] for x in range(m)]

for i in range(m):
    for j in range(n):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

soma = 0
for i in range(m):
    for j in range(n):
       if mat[i][j] >= 0:
        soma = soma + mat[i][j]

print(f"Soma dos positivos: {soma}")

linha = int(input("Escolha uma linha: "))
print("Linha Escolhida: ", end=" ")
for i in range(n):
   print(mat[linha][i], end=" ")

print()

coluna = int(input("Escolha uma coluna: "))
print("Coluna Escolhida: ", end=" ")
for i in range(m):
   print(mat[i][coluna], end=" ")

print()

print("Diagonal Principal: ", end=" ")
for i in range(m):
    print(mat[i][i])

for i in range(m):
    for j in range(n):
        if mat[i][j] < 0:
            alterada[i][j] = mat[i][j] ** 2
        else:
            alterada[i][j] = mat[i][j]

print("Matriz Alterada: ")
for i in range(m):
    for j in range(n):
        print(f"{alterada[i][j]}", end="  ")
    print()


