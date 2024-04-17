#2ª questão

num_inferior = int(input("Digite o número inferior: "))
num_superior = int(input("Digite o número superior: "))
soma_impar = 0

for i in range(num_inferior, num_superior + 1):
  if i % 2 != 0:
    soma_impar += i
print(f"A soma dos números ímpares entre {num_inferior} \
e {num_superior} é: {soma_impar}")
