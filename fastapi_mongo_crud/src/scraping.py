import requests
from bs4 import BeautifulSoup

def champion_italy():
    url = 'https://www.uol.com.br/esporte/futebol/campeonatos/italiano/'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    classificacoes = []
    table = soup.find('table',class_= 'data-table name')
    tbody = soup.find('tbody')
    trs = tbody.find_all('tr')

    for tr in trs:
        spans = tr.find_all('span')
        classificacao = {
            'ranking':spans[0].text,
            'time': spans[2].find('div', class_='visible-sm visible-lg').text
        }
        classificacoes.append(classificacao)

    pontuacao = []
    table2 = soup.find('table',class_= 'data-table score')
    tbody2 = soup.find('tbody',class_= 'score')
    trs2 = tbody2.find_all('tr')

    for tr in trs2:
        tds2 = tr.find_all('td')
        score = {
            'pontos':tds2[0].text,
            'jogos':tds2[1].text,
            'vitorias':tds2[2].text,
            'empates':tds2[3].text,
            'derrotas':tds2[4].text,
            'gols_feitos':tds2[5].text,
            'gols_sofridos':tds2[6].text,
            'saldo_de_gols':tds2[7].text,
            'aproveitamento':tds2[8].text
        }
        pontuacao.append(score)
        
    for classificacao in classificacoes:
        classificacao.update(score)
        result = classificacoes
    return result

    

