#Aluno: Ian Alves Sousa
#DB1 Start
#Exercício 7 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

try:
    lado = float(input('Digite a medida do lado do quadrado em cm: '))
    area = lado * lado
    dobro = area * 2
    print('Um quadrado de lado {}cm tem a área de {}cm² e o dobro dessa área é {}cm².'.format(lado,round(area,1),round(dobro,1)))
except ValueError:
  print('Você não digitou uma medida válida, digite um número!')