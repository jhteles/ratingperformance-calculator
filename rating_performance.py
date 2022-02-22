import pandas as pd

url = "https://raw.githubusercontent.com/jhteles/ratingperformance-calculator/master/tabela_rating_performance.csv"

# Importa a tabela 8.1a do manual da FIDE
df = pd.read_csv(url, sep=';')              # divide em colunas valores separados por ';'

print("Digite o rating dos adversários, separados por espaços: ")

listaRatings = list(map(int, input().split()))  # Cria uma lista com os valores dos ratings a partir do input do usuário

numeroJogos = len(listaRatings)                             # calcula o número de jogos a partir do número de ratings
mediaRating = int(sum(listaRatings)/len(listaRatings))      # valor inteiro da média de ratings

pontos = float(input("Digite a sua pontuação no torneio: "))

p = 1/(numeroJogos/pontos)
p = round(p, 2)                             # Cálculo do valor 'p' da tabela 8.1a

df2 = df.loc[df['p'] == p]['pd'].iloc[0]
pd = df2                                    # Busca na tabela pelo valor 'pd'

ratingPerformance = mediaRating + pd

print(f'Média de rating dos adversários = {mediaRating}')
print(f'Rating Performance no torneio = {ratingPerformance}')
