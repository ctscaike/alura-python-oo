from models.restaurante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato

restaurante_praca = Restaurante('praça','gourmet')
bebida_suco = Bebida('Suco de Abacaxi',5,'grande')
prato_salgado = Prato('Coxinha',8,'Coxinha de Frango')

# restaurante_praca.receber_avaliacao('Gui', 10)
# restaurante_praca.receber_avaliacao('Lais', 8)
# restaurante_praca.receber_avaliacao('Caike', 5)

# restaurante_mexicano = Restaurante('Mexican Food','mexicana')
# restaurante_japones = Restaurante('japin','japonesa')

# restaurante_mexicano.alternar_estado()

def main():
    # Restaurante.listar_restaurantes()
    print(bebida_suco)
    print(prato_salgado)


if __name__ == '__main__':
    main()