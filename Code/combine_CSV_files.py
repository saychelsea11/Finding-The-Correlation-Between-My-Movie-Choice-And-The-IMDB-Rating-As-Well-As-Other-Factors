import pandas as pd

df1 = pd.read_csv(r'2008_2009_movies_filtered.csv',encoding='utf-8')
df2 = pd.read_csv(r'2010_2011_movies_filtered.csv',encoding='utf-8')
df3 = pd.read_csv(r'2012_2013_movies_filtered.csv',encoding='utf-8')
df4 = pd.read_csv(r'2014_to_2019_movies_filtered.csv',encoding='utf-8')

df = df1.append(df2).append(df3).append(df4)
df = df[(df['Like']==1) | (df['Like']==2)]
print (df.shape)

df.to_csv('movies_labeled.csv')



