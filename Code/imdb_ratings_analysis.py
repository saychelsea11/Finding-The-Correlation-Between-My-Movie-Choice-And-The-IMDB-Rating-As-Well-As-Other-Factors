import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Users\Sayan\Google Drive\Data Science\IMDB_Ratings\title_basics.tsv',encoding='utf-8',delimiter='\t')
print (df.head())