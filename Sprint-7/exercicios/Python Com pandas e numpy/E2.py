import pandas as pd
import numpy as np


df = pd.read_csv('actors.csv')

print(f'Media coluna "Number of movies": {df["Number of Movies"].mean()}')
