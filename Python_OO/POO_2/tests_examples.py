class Programa:  # Classe mãe
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__like = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def likes(self):
        return self.__like

    def dar_likes(self):
        self.__like += 1


class Filme(Programa):  # Classe filha
    def __init__(self, nome, ano, duracao):         # Construtor de inicialização da classe filme
        super().__init__(nome, ano)                 # Herança da classe mãe que devolve os métodos
        self.duracao = duracao


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


# ==============================================================================
filme = Filme("hitch", 2012, 140)
filme.dar_likes()
filme.dar_likes()
print(f'{filme.nome} - {filme.duracao}min - {filme.ano} - Likes: {filme.likes}')

serie = Serie("lista negra", 2010, 10)
serie.dar_likes()
serie.dar_likes()
serie.dar_likes()
print(f'{serie.nome} - {serie.temporadas}temp - {serie.ano} - Likes: {serie.likes}')
