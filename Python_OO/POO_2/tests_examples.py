class Programa:  # Classe mãe
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._like = 0

    @property
    def nome(self):
        return self._nome

    @property
    def likes(self):
        return self._like

    def dar_likes(self):
        self._like += 1

    def __str__(self):
        return f'{self._nome} -  {self.likes}'


class Filme(Programa):  # Classe filha
    def __init__(self, nome, ano, duracao):  # Construtor de inicialização da classe filme
        super().__init__(nome, ano)          # Herança da classe mãe que devolve os métodos
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} -  {self.duracao}min - {self.likes}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} -  {self.temporadas} temp - {self.likes}'
# ==============================================================================
filme = Filme("hitch", 2012, 140)  # Objeto
filme.dar_likes()                  # Método dar likes
filme.dar_likes()

serie = Serie("lista negra", 2010, 10)
serie.dar_likes()
serie.dar_likes()
serie.dar_likes()

lista = [filme, serie]

for programa in lista:
    print(programa)
