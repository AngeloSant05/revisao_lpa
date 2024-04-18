#5ª questão

ano_atual = int(2024)

cod_empregado = int(input("Digite sua matricula: "))
ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_ingresso = int(input("Digite o ano de ingresso na empresa: "))
idade = ano_atual - ano_nascimento
tempo_trabalho = ano_atual - ano_ingresso

if (ano_atual - ano_nascimento >= 50 and ano_atual - ano_ingresso) >= 20 \
  or ano_atual - ano_nascimento >= 55 \
  or ano_atual - ano_ingresso >= 25:
  print(f"Você possui {idade} anos e {tempo_trabalho} anos de empresa.\
  Requerer aposentadoria")
else:
  print(f"Você possui {idade} anos e {tempo_trabalho} anos de empresa.\
Não requerer aposentadoria")

