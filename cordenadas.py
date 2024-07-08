x = float(input("Valor de X: "))
y = float(input("Valor de Y: "))

if x > 0 and y > 0:
    print("Posição Q1")
elif x < 0 and y < 0:
    print("Posição Q3")
elif x < 0 and y > 0:
    print("Posição Q2")
elif x > 0 and y < 0:
    print("Posição Q4")
elif y == 0 and x != 0:
    print("Eixo X")
elif x == 0 and y != 0:
    print("Eixo Y")
else:
    print("Origem")