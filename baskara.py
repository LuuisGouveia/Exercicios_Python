import math

a = int(input("Coeficiente A: "))
b = int(input("Coeficiente B: "))
c = int(input("Coeficiente C: "))

delta = b ** 2 - (4 * a * c)

if delta < 0:
    print("A equação não possui raizes reais")
else:
    x1 = - b + math.sqrt(delta) / (2 * a)
    x2 = - b - math.sqrt(delta) / (2 * a)
    print(f"Raiz X1 = {x1:.4f}")
    print(f"Raiz X2 = {x2:.4f}")

