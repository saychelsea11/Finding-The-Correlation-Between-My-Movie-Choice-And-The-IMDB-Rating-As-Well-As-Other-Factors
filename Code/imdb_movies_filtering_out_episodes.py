import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Users\Sayan\Google Drive\Data Science\IMDB_Ratings\2014_to_2019_movies.csv',encoding='utf-8')
df = df[((df['titleType'].str.contains(r'tv')) | (df['titleType'].str.contains(r'video')) | (df['titleType'].str.contains(r'short'))) == False]
df = df[df['genres'].str.contains(r'documentary|Documentary|Sport|sport')==False]
print (df.head())
print (df.shape)
df.to_csv('2014_to_2019_movies_filtered.csv')