#4ª questão

notas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
nota_turma = 0
acima_media = 0

for x in range(0, 15):
  notas[x] = float(input("Digite a nota do aluno: "))
  nota_turma += notas[x]

media_turma = nota_turma / 15

for x in range(0, 15):
  if notas[x] > media_turma:
    acima_media += 1

print(f"A média da turma é: {media_turma}.")
print(f"E a quantidade de alunos acima da média é: {acima_media}")
