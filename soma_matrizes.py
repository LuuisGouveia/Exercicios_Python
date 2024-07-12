m = int(input("Quantas linhas a matriz vai ter?: "))
n = int(input("Quantas colunas a matriz vai ter?: "))

matA = [[0 for x in range(n)]for x in range(m)]
matB = [[0 for x in range(n)]for x in range(m)]
matC = [[0 for x in range(n)]for x in range(m)]


print("Digite os valores da matriz A: ")
for i in range(m):
    for j in range(n):
        matA[i][j] = int(input(f"Elemento[{i},{j}]: "))

print("Digite os valores da matriz B: ")
for i in range(m):
    for j in range(n):
        matB[i][j] = int(input(f"Elemento[{i},{j}]: "))

for i in range(m):
    for j in range(n):
        matC[i][j] = matA[i][j] + matB[i][j]   

print("Matriz gerada: ")
for i in range(m):
    for j in range(n):
        print(f"{matC[i][j]}", end=" ")
    print()

