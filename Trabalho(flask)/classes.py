class Serie:
    def __init__(self, titulo, imagem, sinopse, temporadas, avaliacao, elenco):
        self.titulo = titulo
        self.imagem = imagem
        self.sinopse = sinopse
        self.temporadas = temporadas
        self.avaliacao = avaliacao
        self.elenco = elenco

    

class Tema:
    def __init__(self, nome):
        self.nome = nome
        self.series = []

    def adicionar_serie(self, serie):
        self.series.append(serie)