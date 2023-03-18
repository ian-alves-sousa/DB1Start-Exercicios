# Aluno: Ian Alves Sousa
# DB1 Start - Classes
# Exercício 1 - Escreva uma classe em Python para converter um número inteiro em um numeral romano.

#Criação da classe
class Romano:
    """Clase que recebe um número inteiro e retorna um número romano"""
    s = ''
    def __init__(self,inteiro : int):
        if not (isinstance(inteiro,int) and inteiro > 0):
            raise ValueError(f'A entrada {inteiro} não é um número natural.')
        else:
            self.inteiro = inteiro
            self.__check()
            self.junto = Romano.s.join(self.convertrom)
            
    def converteRomano(self) -> list:
        """Converte o número passado por parâmetro no construtor em uma lista com os números romanos corresponentes desse número"""
        num = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        rom = ['I','IV','V','IX','X','XL','L','LC','C','CD','D','DM','M']
        self.convertrom = []
        i = 12
        numero = self.inteiro
        while i > -1:
            quociente = numero // num[i]
            numero = numero % num[i]
            while quociente != 0:
                self.convertrom.append(rom[i])
                quociente -= 1
            i -= 1
        
    def __check(self):
        """Faz a checagem se é possível converter esse número."""
        if self.inteiro < 3999:
            self.converteRomano()
        else:
            raise ValueError(f'O número {self.inteiro} é maior que 3999, assim, não é possível converte-lo, apenas através de operações com romanos.')
        
    def __str__(self):
        self.__check()
        return f'\nO número {self.inteiro} em romano é: {Romano.s.join(self.convertrom)}' 
    
    def __add__(self, other):
        soma = self.inteiro + other.inteiro
        return Romano(soma)