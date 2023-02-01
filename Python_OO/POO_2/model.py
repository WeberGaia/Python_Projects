"""class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(vingadores.nome)

atlanta = Serie('atlanta', 2018, 2)
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano}')
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return f'{self.nome} - Likes: {self.likes}'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} - Likes: {self.likes} - Duração: {self.duracao}min'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{programa.nome} - Likes: {programa.likes} - {self.temporadas}temp'


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()

lista_store = [vingadores, atlanta]

for programa in lista_store:
    print(programa)
================================================================================
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
        super().__init__(nome, ano)  # Herança da classe mãe que devolve os métodos
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} -  {self.duracao}min - {self.likes}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} -  {self.temporadas} temp - {self.likes}'


class Playlist:
    def __init__(self, nome_playlist, programas):
        self.nome_playlist = nome_playlist
        self._programas = programas

    def __getitem__(self,item):  # Dunder method que utiliza duck typing, ou seja, esta classe possui o comportamento de uma lista sem ser uma lsita
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

# Apaguei alguns métodos que não eram mais necessários


# ==============================================================================
filme = Filme("hitch", 2012, 140)  # Objeto
filme.dar_likes()  # Método dar likes
filme.dar_likes()
filme2 = Filme("PN", 2012, 140)  # Objeto

serie = Serie("lista negra", 2010, 10)
serie.dar_likes()
serie.dar_likes()
serie.dar_likes()

lista = [filme, filme2, serie]

play = Playlist('FDS', lista)

for programa in play:
    print(f'{programa}')

print(f'O tamanho da lista é {len(play)}')
==============================================================================
from collections.abc import MutableSequence

class Minha(MutableSequence):
    def __init__(self, var):
        self.var = var
    def __getitem__(self, item):
        return self.var[item]
    def __len__(self):
        return len(self.var)

    def __delitem__(self, key):
        pass

    def __setitem__(self, key, value):
        pass

    def insert(self, index: int, ) -> None:
        pass

# A classe MinhaListinhaMutavel herda de MutableSequence, ou seja,
# é desejável que o Python avise que tem que implementar todos os
# métodos abstratos de uma MutableSequence. Só que parece que não funcionou.

objetoValido = Minha("      ")

print(len(objetoValido))

    """


