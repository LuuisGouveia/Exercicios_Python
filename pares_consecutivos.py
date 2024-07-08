
while True:
    n = int(input("Digite um numero inteiro: "))
    if n == 0:
        break
    if n % 2 != 0:
        n = n+1
    n = n+(n+2)+(n+4)+(n+6)+(n+8)
    print(f"SOMA = {n}")

