preco = float(input("Preço unitário do produto: "))
quant = int(input("Quantidade comprada: "))
dinheiro = float(input("Dinheiro recebido: "))

valor = preco * quant
troco = dinheiro - valor

print(f"Troco = R$ {troco:.2f}")