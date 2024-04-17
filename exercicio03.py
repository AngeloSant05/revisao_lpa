#3ª questão

soma_precos = float(0)
maior_preco = float(0)
preco = float(0)
for x in range(1, 20+1):
  codigo_produto = int(input("Digite o código do produto: "))
  preco = float(input("Digite o preço do produto: "))
  if preco > maior_preco:
    maior_preco = preco
  soma_precos += preco

media_precos = soma_precos / 20

print("O maior preço é: ", maior_preco)

print("A média dos preços é: ", media_precos)
