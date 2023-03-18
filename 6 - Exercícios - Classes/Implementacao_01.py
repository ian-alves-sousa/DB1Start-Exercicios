#Utilização da classe
from Exercicio_01 import Romano

entrada1 = int(input('Digite um número natural:'))
entrada2 = int(input('Digite outro número natural:'))
n = Romano(entrada1)
n1 = Romano(entrada2)
n2 = n + n1
print(n2)