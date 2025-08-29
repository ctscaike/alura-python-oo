from models.restaurante import Restaurante

restaurante_praca = Restaurante('praça','gourmet')

restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Caike', 5)

restaurante_mexicano = Restaurante('Mexican Food','mexicana')
restaurante_japones = Restaurante('japin','japonesa')

restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()