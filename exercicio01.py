#1ª questão

lucro_menor_5 = 0
produto_menor5 = []
lucro_entre_5_10 = 0
produto_entre5_10 = []
lucro_maior_10 = 0
produto_maior10 = []

total_compra = 0
total_venda = 0
lucro_total = 0

qtd_produtos = int(input("Digite a quantidade de produtos: "))

for x in range(qtd_produtos):
  nome_produto = input("\n" "Digite o nome do produto: ")
  valor_compra = float(input("Digite o valor de compra do produto: "))
  valor_venda = float(input("Digite o valor de venda do produto: "))

  lucro = valor_venda - valor_compra

  porcentagem_lucro = (100 * lucro)/valor_compra

  if porcentagem_lucro < 5:
    lucro_menor_5 += 1
    produto_menor5.append(nome_produto)
  elif porcentagem_lucro >= 5 and porcentagem_lucro <= 10:
    lucro_entre_5_10 += 1
    produto_entre5_10.append(nome_produto)
  else:
   lucro_maior_10 += 1
   produto_maior10.append(nome_produto)

  lucro_total += lucro
  total_compra += valor_compra
  total_venda += valor_venda

print(f"\nQuantidade de produtos com lucro menor que 5%: {lucro_menor_5}.")
print("Os produtos com lucro menor que 5% são:")
for x in range(len(produto_menor5)):
  print(produto_menor5[x])

print(f"\nQuantidade de produtos com lucro entre 5% e 10%: {lucro_entre_5_10}.")
print("Os produtos com lucro entre 5% e 10% são:")
for x in range(len(produto_entre5_10)):
  print(produto_entre5_10[x])

print(f"\nQuantidade de produtos com lucro maior que 10%: {lucro_maior_10}.")
print("Os produtos com lucro maior que 10% são:")
for x in range(len(produto_maior10)):
  print(produto_maior10[x])

print(f"\nValor total de compras: R${total_compra}")
print(f"Valor total de vendas: R${total_venda}")

print(f"\nLucro total: R${lucro_total:}")

