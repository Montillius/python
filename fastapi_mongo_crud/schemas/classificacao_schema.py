def classificacao(dados) -> dict:
    return {
            'id': dados['id'],
            'posicao': dados['posicao'],
            'time': dados['time'],
            'jogos': dados['jogos'],
            'vitorias': dados['vitorias'],
            'empates': dados['empates'],
            'derrotas': dados['derrotas'],
            'gols_feitos': dados['gols_feitos'],
            'gols_sofridos': dados['gols_sofridos'],
            'saldo_de_gols': dados['saldo_de_gols'],
            'aproveitamento': dados['aproveitamento']
    }
    
def tabela_classificacao(entidade)-> list:
        [classificacao(dados) for dados in entidade ]