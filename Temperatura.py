escala = input("Você vai digitar a temperatura em qual escala? (C/F): ")

if escala == "C" or "c":
    temperatura = float(input("Digite a temperatura em Celsius: "))
    conversao = temperatura * 1.8 + 32
    print(f"Temperatura convertida em Fahrenheit: {conversao:.2f}")
elif escala == "F" or "f":
    temperatura = float(input("Digite a temperatura em Fahrenheit: "))
    conversao = (temperatura - 32) / 1.8
    print(f"Temperatura convertida em Celsius: {conversao:.2f}")