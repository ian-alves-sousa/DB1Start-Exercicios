# Aluno: Ian Alves Sousa
# DB1 Start - Tipos não primitivos
# Exercício 10 - Escreva um programa que itere em um dicionário utilizando loops.

dicionario = {}  # Cria um dict vazio
i = 0
while i < 100:  # Estrutura de repetição com grande valor para que mesmo se o número digitado for errado, a pessoa possa tentar outra vez sem perder o que já havia colocado. Retornando em então para o pedido por uma chave.
    try:
        key = int(
            input('\n-----Digite a chave do dicionário(Digite 0 para finalizar): '))
        if key == 0:  # Finaliza a estrutura de repetição e mostra o dicionário caso o número da chave for 0
            print('Você finalizou o dicionário.')
            break
        valor = int(input(f'Digite o valor da chave {key}: '))
        if key not in dicionario.keys():  # Verifica se a chave está na visão do dicionário das chaves
            print(
                f'A chave {key} foi adicionada no dicionário com o valor {valor}.')
        else:
            print(
                f'A chave {key} já existia no dicionário, por tal, atualizamos o valor dela para {valor}.')
            # Se a chave já existir no dicionário, a mesma será adicionada e o seu valor terá prioridade, substituindo o anterior
        dicionario[key] = valor  # Adiciona o par chave valor no dicionário
        i += 1
    except ValueError:
        print('\nDigine números inteiros')

#A resolução desse exercício utiliza-se do exercício 7 novamente, e retorna ao usuário os valores das chaves e os valores inseridos. Realizando uma iteração em um dicionário utilizando loops.
for k,v in dicionario.items():
  print(f'\nA chave {k} tem o valor {v}.')