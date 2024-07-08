import math

base = int(input("Digite a base do retangulo: "))
altura = int(input("Digite a altura do retangulo: "))

area = base * altura

diagonal = math.sqrt(base ** 2 + altura ** 2)

perimetro = 2 * (base + altura) 

print(f"Area do retangulo: {area}")
print(f"Perimetro do retangulo: {perimetro}")
print(f"Diagonal do retangulo: {diagonal:.4f}")