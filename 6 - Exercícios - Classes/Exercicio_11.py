# Aluno: Ian Alves Sousa
# DB1 Start - Classes
# Exercício 11 - Criar uma classe que representará outro tipo de aeronave militar, com o nome JatoMilitar2Lugares. O método construtor deverá receber duas informações: o modelo, e a base onde a aeronave está; Cria um método chamado designar_piloto que deverá contar o nome do piloto. Por regra, o primeiro piloto será considerado o piloto principal e o segundo, o seu copiloto. Depois de informados os dois nomes, não poderá ser inserido mais nenhum nome.
# Criar um método rebasear_aeronave, que receberá como parâmetro o nome da base para onde a aeronave deverá ser enviada. Antes de registrar, é necessário validar se dois pilotos foram designados para a aeronave, e somente se ambos tiverem sido designados, registrar o rebaseamento, com a data e hora da movimentação.
#Sobrescreva o métod __str__ da classe, para imprimir o seguinte conteúdo:
#Jato: <NOME DA AERONAVE>
#Base inicial: <NOME DA BASE DE ORIGEM>
#Piloto: <NOME DOS PILOTOS DESIGNADOS>
#Histórico de transferências: <LISTAGEM DAS BASES PELAS QUAIS A AERONAVE PASSOU MOSTRANDO A DATA / HORA E BASE>

from Exercicio_10 import JatoMilitar1Lugar
#Criação da classe
class JatoMilitar2Lugares(JatoMilitar1Lugar):
    """Classe para criar um modelo e histórico de um Jato Militar de 2 lugares."""
    def __init__(self, modelo: str, base: str):
        """Inicializa a instância, faz a checagem das entradas e define o as variáveis de instância."""
        super().__init__(modelo, base)
        self._piloto2 = None
        self.completed = None
      
    def designar_piloto(self, piloto: str):
        """Designa os dois pilotos em ordem de inserção e não permitindo alterar os pilotos após isso."""
        if self.completed is True:
            print(f'Os dois pilotos já foram setados: {self._piloto} e {self._piloto2}')
        else:
            if (self._piloto2 is None and self._piloto is None):
              super().designar_piloto(piloto)
            elif self._piloto2 is None:
              self._piloto2 = piloto
              self.completed = True

    def rebasear_aeronave(self, new_base: str):
        """Faz o rebaseamento da nave se tiver piloto e ciar um histórico de rebaseamento."""
        if self.completed is True:
          super().rebasear_aeronave(new_base)
        else:
           print(f'Não é possível rebasear o jato sem definir os dois pilotos primeiro.')

    @property
    def piloto2(self):
        return self._piloto2
    
    @piloto2.setter
    def piloto2(self, piloto):
        raise NotImplementedError(f'Não é possível setar o nome do piloto dessa forma, utilize o método designar_piloto.')

    def __str__(self) -> str:
        """Define o que será printado de acordo com as informações que já foram setadas."""
        if (self.completed == None and self._new_base == None):
            return f"""Jato: {self.modelo}
Base inicial: {self.base}"""
        elif self._new_base == None:
            return f"""Jato: {self.modelo}
Base inicial: {self.base}
Piloto: {self._piloto} e {self._piloto2}
Histórico de transferências: Não há históricos de transferências."""
        else:
            return f"""Jato: {self.modelo}
Base inicial: {self.base}
Piloto: {self._piloto} e {self._piloto2}
Histórico de transferências: {self._historico}"""
        
#Implementação da classe
jato = JatoMilitar2Lugares('Jato','Manguaratiba')
jato.designar_piloto('Neymar')
jato.designar_piloto('Cebola')
jato.rebasear_aeronave('Paris')
jato.rebasear_aeronave('Quatar')
print(jato)
