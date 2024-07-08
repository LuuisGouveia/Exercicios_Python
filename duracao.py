duracao = int(input("Digite a duração em segundos: "))

resto = duracao % 3600
horas = duracao / 3600
minutos = resto / 60
segundos = resto % 60

print(f"{horas:.0f}:{minutos:.0f}:{segundos:.0f}")
