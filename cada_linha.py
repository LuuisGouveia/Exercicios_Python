m = int(input("Qual a ordem da matriz: "))
n = m

mat = [[0 for x in range(n)]for x in range(m)]

for i in range(m):
    for j in range(n):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

maior = [0 for x in range(m)]

for i in range(m):
    for j in range(n):
        if mat[i][j] > maior[i]:
            maior[i] = mat[i][j]

print("Maior de cada linha: ")
for i in range(m):
    print(maior[i])
