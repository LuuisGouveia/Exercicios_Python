

idade = 0
soma = 0
count = 0
while idade >= 0:
    idade = int(input("Digite a idade: "))
    if idade > 0:
        soma = soma + idade
    count = count + 1

media = soma / (count-1)

print(f"Media das idades: {media:.2f}")