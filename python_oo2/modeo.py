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
        return f'Nome: {self.nome} Likes: {self.likes}'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}'


class PlayList(list):
    def __init__(self, nome, programas):
        self.nome = nome
        self.programas = programas
    def tamanho(self):
        return len(self.programas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
tmep = Filme('Todo mundo em pánico', 1999, 100)

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()

supernatural = Serie('supernatural', 2012, 12)
demolidor = Serie('Demolidor', 2016, 2)


supernatural.dar_likes()
supernatural.dar_likes()

demolidor.dar_likes()
demolidor.dar_likes()


filmes_series = [demolidor, tmep, supernatural, vingadores]
playlist_fim_semna = PlayList('Fim de Semana', filmes_series)

for programa in playlist_fim_semna.programas:
    print(programa)
