n = int(input("Quantas pessoas serão digitadas?: "))

count = 0
menores = 0
soma = 0
nome = [0 for x in range(n)]
idade = [0 for x in range(n)]
altura = [0 for x in range(n)]

for i in range(0, n):
    print(f"Digite os dados da {i+1}a Pessoa: ")
    nome[i] = input("Nome: ")
    idade[i] = int(input("Idade: "))
    if idade[i] < 16:
        menores = menores + 1
    altura[i] = float(input("Altura: "))
    soma = soma + altura[i]
    count = count + 1

media = soma / count

percentual = menores * 100 / count

print(f"Altura Media = {media}")
print(f"Percentual de pessoas com menos de 16 anos = {percentual}")

for i in range(n):
    if idade[i] < 16:
        print(nome[i])