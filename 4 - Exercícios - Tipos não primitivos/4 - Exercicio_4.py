# Aluno: Ian Alves Sousa
# DB1 Start - Tipos não primitivos
# Exercício 4 - Escreva um programa que conte o número de caracteres de uma string ( Exemplo:'google.com'Resultado Esperado: {'o': 3,'g': 2,'.': 1,'e': 1,'l': 1,'m': 1,'c': 1} )

string = input('Digite uma string: ') #Solicita uma entrada em string
string = string.lower() #Tiras as letras maiúsculas da string
listaString = list(string) #Transforma a string em uma lista com cada caractere
qtde = []
for letra in listaString: #Faz a contagem de quantas vezes cada string aparece
  contagem = listaString.count(letra)
  qtde.append(contagem) #Adiciona esse valor no final da lista qtde
  
comparacao = [[listaString[i], qtde[i]] for i in range(len(qtde))] #Cria uma lista onde cada posição tem dois números, o caractere e a quantidade correspondente dele na string.
dicionario = {k:v for (k,v) in comparacao} #Cria um dicionário baseado na comparação, e o dicionário faz com que as letras repetidas sejam sobrepostas
for k,v in dicionario.items(): #Printa o caracte e a quantidade baseada na visão do dicionário
  if v == 1:
    print(f'O caracter \'{k}\' aparece {v} vez em {string}.')
  else:
    print(f'O caracter \'{k}\' aparece {v} vezes em {string}.')