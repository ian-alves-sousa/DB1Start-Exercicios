# Aluno: Ian Alves Sousa
# DB1 Start - Classes
# Exercício 2 - Escreva uma classe em Python para converter um número romano em um número inteiro.

from Exercicio_01 import Romano
#Criação da classe
class Inteiro():
    """Classe que recebe um número romano e retorna um número inteiro."""
    rom = ['M','D','C','L','X','V','I']
    num = [1000,500,100,50,10,5,1]
    def __init__(self,romano : str):
        romano = romano.upper()
        self.__check(romano)
        self.soma = self.converteInteiro()
        self.final_check(romano)
            
    def __check(self,romano):
        """Faz a checagem se os algarismos do número romano existem."""
        for i in list(romano):
            if i not in Inteiro.rom:
                raise ValueError(f'A entrada {romano} não é número romano.')
        self.romano = list(romano)
        
    def final_check(self,romano):
        """Checagem final - Vê se o número de entrada é um romano válido, coparando com a entrada com a saída da operação inversa."""
        if not Romano(self.soma).junto == romano:
            raise ValueError(f'A entrada {romano} não é um número romano válido.')
        
    def converteInteiro(self) -> int:
        """Faz a conversão do romano e retorna um inteiro."""
        dicionario = dict(zip(Inteiro.rom,Inteiro.num))
        soma = 0
        pula = False
        for i in range(len(self.romano)-1,-1,-1):
            if (dicionario[self.romano[i]] > dicionario[self.romano[i-1]]) and i != 0:
               soma = soma + dicionario[self.romano[i]] - dicionario[self.romano[i-1]]
               pula = True
            elif pula == True:
                pula = False
                continue
            elif self.romano[i] in dicionario.keys():
                soma += dicionario[self.romano[i]]
                pula = False
        return soma
                
    def __str__(self):
        s = ''
        return f'O número romano {s.join(self.romano)} convertido em inteiro é: {self.soma}'
        
#Implementação da classe
entrada = input('Digite um número romano:')       
x = Inteiro(entrada)
print(x)