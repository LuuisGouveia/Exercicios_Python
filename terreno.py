largura = int(input("Digite a largura do terreno: "))
comprimento = int(input("Digite o comprimento do terreno: "))
valor = float(input("Digite o valor do m2: "))

area = largura * comprimento
preco = valor * area

print(f"A area do terreno é de {area} m2 ")
print(f"O valor do terreno é de R$ {preco:.2f} reais")

