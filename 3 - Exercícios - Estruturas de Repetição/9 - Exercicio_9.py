# Aluno: Ian Alves Sousa
# DB1 Start - Estruturas de Repetição
# Exercício 9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.

x = 0
while x < 3:
    try:  # Deixa as entradas em um loop, até a entrada não ser a correta, o sistema não pede a próxima
        if x == 0:
            # Define o primeiro valor como o maior e menor valor
            maior = menor = meio = n1 = float(
                input('Digite o primeiro número: '))
        elif x == 1:
            n2 = float(input('Digite o segundo número: '))
        else:
            n3 = float(input('Digite o terceiro número: '))
        x += 1
    except ValueError:
        print('Você não digitou um número.')

n_list = (n1, n2, n3)
contagemMaior = 0
for i in range(1, 3):  # Faz duas iterações e compara o valor do n1 com os outros 2
    if maior <= n_list[i]: #Igual colocado para suprir a necessidade de quando alguém colocar valores iguais e considerar como se fosse o maior. Assim temos a noção posterior de que o meio é o n2 ou não.
      maior = n_list[i]  # Substitui o valores do maior quando for maior.
      contagemMaior += 1
    if menor > n_list[i]:
      menor = n_list[i] # Substitui o valores do menor quando for menor
    if maior > n_list[i] > menor: #Condição para quando o meio se mantém no n1, muda para n3 ou vai para o n2
      meio = n_list[i] #Quando o n3 for o do meio, ele receberá o meio
    elif maior >= n_list[i] >= menor and contagemMaior != 1: #Para o n2 ser o do meio é preciso que ele esteja entre n1 e n3 e que o maior não tenha se movimentado apenas uma vez. Pois se isso aconteceu, quer dizer que o meio está no n1, e não no n2, já que não é o n3, visto da última condição.
      meio = n_list[i-1]
    
else:
    print(f'A ordem decrescente dos números é: {maior}, {meio}, {menor}.')
