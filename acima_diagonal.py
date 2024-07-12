m = int(input("Qual a ordem da matriz?: "))
n = m

mat = [[0 for x in range(n)]for x in range(m)]

for i in range(m):
    for j in range(n):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

soma = 0
for i in range(m):
    for j in range(i+1, n):
        soma = soma + mat[i][j]

print(f"Soma dos numeros acima da diagonal principal: {soma}")