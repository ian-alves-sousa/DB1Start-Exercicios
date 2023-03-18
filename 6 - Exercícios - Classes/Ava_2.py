from enum import Enum 

 

 

class Setor(Enum): 

    ELETRODOMESTICOS = 'ELETRODOMESTICOS' 

    ELETRONICOS = 'ELETRONICOS' 

    VESTUARIO = 'VESTUARIO' 

 

 

class Vendedor: 

    __salarios = { 

        Setor.ELETRODOMESTICOS: 5000, 

        Setor.ELETRONICOS: 7000, 

        Setor.VESTUARIO: 4000, 

    } 

 

    def __init__(self, nome: str, setor: Setor): 

        self.nome = nome 

        self.setor = setor 

 

    def obter_salario(self) -> float: 

        return self.__salarios[self.setor] 

 

 

class VendedorComissionado(Vendedor): 

 

    def __init__(self, nome: str, setor: Setor): 

        super().__init__(nome, setor) 

        self.__vendas = 0 

 

    def registrar_venda(self, valor: float): 

        self.__vendas += valor 

 

    def obter_salario(self) -> float: 

        salario_base = super().obter_salario() 

        return salario_base + self.obter_comissao() 

 

    def obter_comissao(self) -> float: 

        return self.__vendas * 0.05
    

def exibir_salario(vendedor: Vendedor): 

    print(f"O salário de {vendedor.nome} é {vendedor.obter_salario()}") 

 
 
vendedor_a = Vendedor('Vendedor A', Setor.VESTUARIO) 

vendedor_b = VendedorComissionado('Vendedor B', Setor.ELETRODOMESTICOS) 

vendedor_b.registrar_venda(25000) 
 
exibir_salario(vendedor_a) 
exibir_salario(vendedor_b) 