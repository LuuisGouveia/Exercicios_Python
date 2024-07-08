nota1 = float(input("Digite a primeira nota: "))
while nota1 < 0 or nota1 > 10:
    print("Valor invalido")
    nota1 = float(input("Tente novamente: "))

nota2 = float(input("Digite a segunda nota: "))
while nota2 < 0 or nota2 > 10:
    print("Valor invalido")
    nota2 = float(input("Tente novamente: "))

media = (nota1 + nota2) / 2

print(f"Media do aluno: {media:.2f}")