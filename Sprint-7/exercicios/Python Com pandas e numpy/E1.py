import pandas as pd
import numpy as np

# Lendo o arquivo CSV
df = pd.read_csv('actors.csv')


AtorComMaisFilmes = np.argmax(df['Number of Movies'])
Numerofilmes = df.loc[AtorComMaisFilmes, 'Number of Movies']

print(f'O ator/atriz com o maior número de filmes é {df.loc[AtorComMaisFilmes, "Actor"]} com {Numerofilmes} filmes.')



