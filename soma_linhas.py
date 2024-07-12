m = int(input("Quantas linhas a matriz vai ter? "))
n = int(input("Quantas colunas a matriz vai ter? "))

mat = [[0 for x in range(n)] for x in range(m)]
vet = [0 for x in range(m)]


for i in range(m):
    print(f"Digite os dados da {i+1}a linha: ")
    for j in range(n):
        mat[i][j] = int(input())

for i in range(m):
    vet[i] = 0
    for j in range(n):
        vet[i] = vet[i] + mat[i][j]

print("Vetor Gerado: ")
for i in range(m):
    print(vet[i])
