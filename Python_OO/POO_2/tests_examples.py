"""
Inicialmente, vamos recriar todos os exemplos e fazer testes do tema: Python orientado a objetos.

1) Criar uma classe
    1,1: inicializar variáveis.
    1,2: criar um método getter e um setter.
            @property
            def nome(self):
                return print(f"o nome do filme é {self._nome}")
            @nome.setter
            def nome(self, nome):
                self._nome = nome


"""


class Filme:
    def __init__(self, nome, duracao, ano):
        self._nome = nome
        self.duracao = duracao
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    def dar_likes(self):
        self._likes += 1

    @property
    def dar_likes2(self):
        return self._likes

    def __str__(self):
        return f"{self._nome} - likes: {self._likes} - duração: {self.duracao}min"


filme1 = Filme("Avengers", 140, 2013)
filme1.dar_likes()
filme1.dar_likes()
filme1.dar_likes()
filme1.dar_likes()
filme1.dar_likes()
filme1.dar_likes()

print(filme1)
