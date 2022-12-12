class Selecao:
    def __init__(self, nome, pontos, vitorias, empates, derrotas, gols_pro, gols_contra, grupo):
        self.nome = nome
        self.pontos = pontos
        self.vitorias = vitorias
        self.empates = empates
        self.derrotas = derrotas
        self.gols_pro = gols_pro
        self.gols_contra = gols_contra
        self.saldo_gols = gols_pro - gols_contra
        self.aproveitamento = (self.pontos / (self.vitorias + self.empates + self.derrotas)) * 100
        self.grupo = grupo

    def __str__(self):
        return self.nome


class Partida:
    def __init__(self, data, hora, casa, visitante, placar_casa, placar_visitante, posse_bola_casa, 
                    posse_bola_visitante, amarelos_casa, amarelos_visitante, vermelhos_casa, vermelhos_visitante,
                    no_passes_casa, no_passes_visitante, no_escanteios_casa, no_escanteios_visitante):

        self.data = data
        self.hora = hora

        self.casa = casa
        self.visitante = visitante

        self.placar_casa = placar_casa
        self.placar_visitante = placar_visitante

        self.posse_bola_casa = posse_bola_casa
        self.posse_bola_visitante = posse_bola_visitante

        self.amarelos_casa = amarelos_casa
        self.amarelos_visitante = amarelos_visitante
        self.vermelhos_casa = vermelhos_casa
        self.vermelhos_visitante = vermelhos_visitante

        self.no_passes_casa = no_passes_casa
        self.no_passes_visitante = no_passes_visitante

        self.no_escanteios_casa = no_escanteios_casa
        self.no_escanteios_visitante = no_escanteios_visitante

    def __str__(self):
        return self.casa + " x " + self.visitante


class Grupo:
    def __init__(self, nome, partidas):
        self.nome = nome
        self.partidas = partidas

    def __str__(self):
        return self.nome