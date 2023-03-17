#Aluno: Ian Alves Sousa
#DB1 Start - Estruturas Condicionais
#Exercício 10 - Faça um programa para o cálculo de uma folha de pagamento

lista1 = ['Ana', 'Alberto', 'Roberto']
lista2 = ['Caique', 'Mônica', 'Larissa']
lista3 = ['Guilherme', 'Gabiel', 'Fernanda']

lista = [lista1, lista2, lista3]

if lista1 in lista:
  print(f'O salário da(o) {lista1[0]} é de R$3.000,00.')
  print(f'O salário da(o) {lista1[1]} é de R$3.000,00.')
  print(f'O salário da(o) {lista1[2]} é de R$3.000,00.')
if lista2 in lista:
  print(f'O salário da(o) {lista2[0]} é de R$3.500,00.')
  print(f'O salário da(o) {lista2[1]} é de R$3.500,00.')
  print(f'O salário da(o) {lista2[2]} é de R$3.500,00.')
if lista3 in lista:
  print(f'O salário da(o) {lista3[0]} é de R$4.000,00.')
  print(f'O salário da(o) {lista3[1]} é de R$4.000,00.')
  print(f'O salário da(o) {lista3[2]} é de R$4.000,00.')