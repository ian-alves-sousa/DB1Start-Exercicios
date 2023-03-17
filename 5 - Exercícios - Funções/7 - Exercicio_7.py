# Aluno: Ian Alves Sousa
# DB1 Start - Funções
# Exercício 7 - Escreva um programa Python que execute uma string que contenha um código Python.

#A função recebe uma string que contem um código Python e o executa
def Python(string : str):
    """Executa um código em Python"""
    exec(string)



string = """
try:
  n1 = int(input('Digite um número inteiro: '))

  if n1 > 0:
    print(f'O número é {n1} é positivo.')
  elif n1 < 0:
    print(f'O número é {n1} é negativo.')
  else:
    print(f'Você digitou {n1} é ele é neutro.')

except ValueError:
  print('Você não digitou um número inteiro. Tente novamente.')
"""
#Na primeira vez que é chamado, a função Python recebe uma string com um código completo e o executa sem problemas.
Python(string)
#Na segunda vez que é chamado, o programa solicita uma linha de código e o executa.
string = input("""Escreva seu código:
""")
Python(string)

#Realizei tentativas onde é solicitado um cógigo completo com várias intruções, estruturas de repetição, condicionais e tudo mais, contudo, quando faço uam estrutura onde isso é colocado, a função exec não entende a identação em que eu coloco no terminal, e por tal ocorre um erro. Se você souber como me ajudar a resolver, crie uma Issue or Pull Request e me ajude!

