from models.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return 'ativado' if self._ativo else 'inativo'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    # @ property disponibiliza o método para cada objeto instanciado
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self.avaliacao)
        qtd_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / qtd_de_notas, 1)
        return media

# restaurante_praca = Restaurante('Praça','Gourmet')
# restaurante_praca.nome = 'Praça'
# restaurante_praca.categoria = 'Gourmet'

# restaurante_pizza = Restaurante('Pizza Express','Italiana')

# restaurantes = [restaurante_praca, restaurante_pizza]

# # dir exibe atributos e métodos
# # print(dir(restaurante_praca))

# # vars exibe um dicionário com os valores atribuídos "manualmente" às variáveis
# print(vars(restaurante_praca))
# print(restaurante_pizza)

# Restaurante.listar_restaurantes()

