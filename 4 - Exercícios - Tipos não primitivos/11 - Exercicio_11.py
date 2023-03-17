# Aluno: Ian Alves Sousa
# DB1 Start - Tipos não primitivos
# Exercício 11 - Escreva um programa que remova itens duplicados de uma lista.

lista = []  # Cria uma lista vazia
for i in range(100):  # Define um número de iterações alto para que quem for testar não saia do for até chegar o break
    try:
        # Acrescenta o valor ao final da lista
        lista.append(float(input('Digite um valor (para parar a lista digite 0): ')))

        if lista[0] != 0:
          # Compara o valor colocado com 0, se for 0, o deleta, printa a lista a finaliza.
          if lista[len(lista)-1] == 0:
            del lista[len(lista)-1]
            break
        else: #Se o primeiro número for 0, precisa de outra entrada para parar a formação da lista.
            del lista[0]
            print('Você criou uma lista vazia, adicione um número para.')

    except ValueError:  # Se for digitado algum valor diferente de floar vai dar essa mensagem.
        print('Valor inválido. Tente novamente!')

cont = 0
tamanho = len(lista) #Guarda o valor do tamanho da lista atual, pois ao tirar os repetidos, ese tamanho será menor.
for i in range(tamanho):
  if (tamanho - cont) > i: #Acontece até que o número da len(lista) seja atigindo, ou seja, não tem mais números repetidos
    rep = lista.count(lista[i]) #Guarda o valor de quantas repetições tem esse valor na lista
    if rep > 1:
      for j in range(rep-1): #Estrutura de repetição para tirar todos os números repetidos, e irá se repetir na quantidade de números repetidos tiver
        pos = lista.index(lista[i],i+1,len(lista)) #pos recebe a posição do próximo númerio que é igual a lista[i], depois da posição i até o final
        del lista[pos] #Sabendo onde a repetição se encontra, podemos retirar ela da lista e acrescentar a contagem, afirmando que o tamanho a lista foi diminuido
        cont += 1
  else: #Assim que o tamanho da lista for igual ao número de valores sem repetições sai do for
    break  
  
print(f'\nA lista digida sem valores repedidos é: \n{lista}')
 

