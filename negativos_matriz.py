m = int(input("Quantas linhas a matriz vai ter?: "))
n = int(input("Quantas colunas a matriz vai ter?: "))

mat = [[0 for x in range(n)] for x in range(m)]

for i in range(m):
    for j in range(n):
        mat[i][j] = int(input(f"Elemento[{i},{j}]: "))

print("Negativos da matriz: ")
for i in range(m):
    for j in range(n):
        if mat[i][j] < 0:
            print(mat[i][j])
    
