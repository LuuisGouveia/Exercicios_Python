n1 = int(input("primeiro numero: "))
n2 = int(input("segundo numero: "))

if n1 > n2 :
    n3 = n1
    n1 = n2
    n2 = n3
soma = 0

for i in range(n1+1, n2):
    if i % 2 != 0:
        soma = soma + i

print(f"Soma dos impares: {soma}")