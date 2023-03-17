#Aluno: Ian Alves Sousa
#DB1 Start - Estruturas Condicionais
#Exercício 4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

try:
  letra = str(input('Digite UMA letra: '))
  vogal = ['a','e','i','o','u','A','E','I','O','U']
  consoante = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
  tamanho = len(letra)

  if tamanho == 1:
    if letra[0] in vogal:
      print(f'A letra {letra} é uma vogal.')
    elif letra[0] in consoante:
      print(f'A letra {letra} é uma consoante.')
    else:
      print(f'o que você digitou não é vogal ou consoante.')
  else:
    print('Você digitou mais de uma letra.')

except ValueError:
  print(f'Você digitou algo diferente de UMA letra.')