# Aluno: Ian Alves Sousa
# DB1 Start - Classes
# Exercício 3 - Escreva uma classe em Python que leia dois números e implemente uma exponenciação.

class Exp():
    """Classe criada para ler dois números e implementar uma exponenciação"""
    def __init__(self,base:float,expoente:float):
        """Inicializa a função verificando as entradas se são números inteiros ou decimais."""
        if not (isinstance(base,int) or isinstance(base,float)):
            raise ValueError(f'O valor de entrada de {base} não está correto.')
        elif not (isinstance(expoente,float) or isinstance(expoente,int)):
            raise ValueError(f'O valor de entrada de {expoente} não está correto.')
        self.base = base
        self.expoente = expoente
        self.exp = self.exponenciacao()
        
    def exponenciacao(self):
        """Realiza a exponenciação, base elevado ao expoente."""
        exp = self.base ** self.expoente
        self.inversa = False
        return round(exp,2)
        
    def exponenciacao_inversa(self):
        """Solicita uma exponenciação inversa, expoente elevado a base."""
        exp = self.expoente ** self.base
        self.inversa = True
        return round(exp,2)
    
    def __str__(self):
        """Define o que será printado de acordo com a exponenciação realizada"""
        if self.inversa == False:
            return f'O valor de {self.base} elevado a {self.expoente} é: {self.exp}'
        else:
            return f'O valor de {self.expoente} elevado a {self.base} é: {self.exponenciacao_inversa()}'
        

#Implementação da classe
x = Exp(8,2)
x.exponenciacao_inversa()
x.exponenciacao()
print(x)