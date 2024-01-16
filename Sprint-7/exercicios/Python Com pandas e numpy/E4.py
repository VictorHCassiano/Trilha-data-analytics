import pandas as pd

df = pd.read_csv('actors.csv')

most_frequent_movies = df['#1 Movie'].value_counts()

print(most_frequent_movies.head(5).to_string())
