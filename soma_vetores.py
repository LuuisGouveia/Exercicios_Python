n = int(input("Quantos numeros o vetor vai ter?: "))

vet1 = [0 for x in range(n)]
vet2 = [0 for x in range(n)]
soma = [0 for x in range(n)]

print("Digite os valores do primeiro vetor: ")
for i in range(n):
    vet1[i] = int(input())

print("Digite os valores do segundo vetor: ")
for i in range(n):
    vet2[i] = int(input())

for i in range(n):
    soma[i] = vet1[i] + vet2[i]

print("Vetor Gerado: ")
for i in range(n):
    print(soma[i])

