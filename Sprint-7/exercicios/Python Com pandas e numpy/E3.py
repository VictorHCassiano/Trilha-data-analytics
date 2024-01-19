import pandas as pd
import numpy as np

df = pd.read_csv('actors.csv')

MaiorAvgPorFilme = np.argmax(df['Average per Movie'])

print(f'O ator/atriz com a maior média de faturamento por filme é {df.loc[MaiorAvgPorFilme, "Actor"]} com {df.loc[MaiorAvgPorFilme, "Average per Movie"]} de média por filme.')