# Construção de uma lista de filmes e séries como na netflix utilizando Orientação a Objetos

class Programa:                                             # Classe mãe
    def __init__(self, nome, ano, ator_principal):          # Inicializador da classe mãe
        self._nome = nome.title()                           # Atributos
        self._ano = ano
        self._ator_principal = ator_principal.title()
        self.like = 0

    def likes(self):
        self.like += 1

    @property                                               # Métodos de aquisição de dados (Getter)
    def nome(self):
        return self._nome

    @property
    def darlikes(self):
        return self.like

    @property
    def ano(self):
        return self._ano

    @property
    def ator(self):
        return self._ator_principal

    def __str__(self):                                      # Permite a manipulação de Strings
        return f"{self._nome} - {self.like} "


class Filme(Programa):                                      # Classe Filha
    def __init__(self, nome, ano, duracao, ator_principal):  # Inicializador da classe filha
        super().__init__(nome, ano, ator_principal)          # Herança dos atributos da classe mãe
        self._duracao = duracao

    def __str__(self):
        return f"{self.nome} - {self._ano} - {self._duracao}min - {self._ator_principal}\n" \
               f"Likes: {self.like}"


class Serie(Programa):
    def __init__(self, nome, ano, temporadas, ator_principal):
        super().__init__(nome, ano, ator_principal)
        self._temporadas = temporadas

    def __str__(self):
        return f"{self.nome} - {self._ano} - {self._temporadas}temp. - {self._ator_principal}\n" \
               f"Likes: {self.like}"


class Playlist:
    def __init__(self, nome_playlist, lista_favorita):
        self.nome_playlist = nome_playlist
        self.lista_favorita = lista_favorita

    def __getitem__(self, item):
        return self.lista_favorita[item]

    def __len__(self):
        return len(self.lista_favorita)
