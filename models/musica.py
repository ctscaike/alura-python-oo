class Musica:
    faixa = []
    
    def __init__ (self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

musica1 = Musica('Bohemian Rhapsody','',355)
# musica1.nome = 'Bohemian Rhapsody'
# musica1.duracao = 355

print(vars(musica1))