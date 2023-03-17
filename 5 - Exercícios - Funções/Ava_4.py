def calcular_somar(num):
    soma = 0
    for i in range(0,num+1,2):
        soma += i
    return soma

num = int(input('Digite um número positivo: '))
print(calcular_somar(num))