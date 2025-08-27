from models.restaurante import Restaurante

restaurante_praca = Restaurante('praça','gourmet')
restaurante_mexicano = Restaurante('Mexican Food','mexicana')
restaurante_japones = Restaurante('japin','japonesa')

restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()