#Aluno: Ian Alves Sousa
#DB1 Start - Estruturas Condicionais
#Exercício 3 - Faça um Programa que verifique se uma letra digitada é "F"ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

print('''Escolha seu sexo: 
F - Feminino
M - Masculino         ''')
sx = input('Digite a letra correspondente ao seu sexo: ')

if sx == 'F' or sx == 'f':
  print(f'Você é do sexo feminino.')
elif sx == 'M' or sx == 'm':
  print(f'Você é do sexo masculino.')
else:
  print(f'O sexo digitado é invalido.')
