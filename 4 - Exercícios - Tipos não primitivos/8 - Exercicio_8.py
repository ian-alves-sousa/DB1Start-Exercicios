# Aluno: Ian Alves Sousa
# DB1 Start - Tipos não primitivos
# Exercício 8 - Escreva um programa que concatene os dicionários abaixo e crie um novo. Exemplo dicionário(Dict): dic1={1:10, 2:20}, dic2={3:30, 4:40}, dic3={5:50,6:60}
# Resultado esperado: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dicionario1 = {} #Cria um dict vazio
dicionario2 = {} #Cria um dict vazio
dicionario3 = {} #Cria um dict vazio
lista = [dicionario1,dicionario2,dicionario3] #Cria uma lista de dicionários
for j in lista: #Seleciona cada dicionário da lista
  i = 0 #Zera o 1 para que quando voltar ao for, o while funcione novamente
  while i < 100: #Estrutura de repetição com grande valor para que mesmo se o número digitado for errado, a pessoa possa tentar outra vez sem perder o que já havia colocado. Retornando em então para o pedido por uma chave.
      try:
          key = int(input(f'\n-----Digite a chave do Dicionário {lista.index(j)+1} (Digite 0 para finalizar): '))
          if key == 0: #Finaliza a estrutura de repetição e mostra o dicionário caso o número da chave for 0
              print(f'Você finalizou o Dicionário {lista.index(j)+1} - {j}.')
              break
          valor = int(input(f'Digite o valor da chave {key}: '))
          if key not in j.keys(): #Verifica se a chave está na visão do dicionário das chaves
              print(f'A chave {key} foi adicionada no Dicionário {lista.index(j)+1} com o valor {valor}.')
          else:
              print(f'A chave {key} já existia no Dicionário {lista.index(j)+1}, por tal, atualizamos o valor dela para {valor}.')
              #Se a chave já existir no dicionário, a mesma será adicionada e o seu valor terá prioridade, substituindo o anterior
          j[key] = valor #Adiciona o par chave valor no dicionário
          i += 1
      except ValueError:
          print('\nDigine números inteiros.')

          

print(f'\nOs dicionários criados foram: {lista[0]},{lista[1]},{lista[2]}')
#Realiza a concateção dos dicionários, a chave mais recente à ser adiciona tem prioridade
concatenado = dicionario1 | dicionario2 | dicionario3
print(f'\nA concatenação dos dicionários tem o seguinte resultado: {concatenado}.')
