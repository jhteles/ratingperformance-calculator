import pandas as pd

# Importa a tabela 8.1a do manual da FIDE
df = pd.read_excel(r'C:\Users\joseh\Documents\tabela_rating_performance.xlsx')
# place "r" before the path string to address special character, such as '\'. //

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
