import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('netflix_titles.csv', delimiter=',',
                   usecols=['release_year']).value_counts().to_frame()\
                   .sort_values(by='release_year').reset_index().\
                   rename(columns={'release_year': 'Release Year',
                                   0: 'Amount'})
data.plot(x='Release Year', y='Amount', rot=90, figsize=(15, 10), grid=True,
          color='red')
plt.xlabel('Release Year', fontsize=15)
plt.ylabel('Amount of released movies', fontsize=15)
plt.title('Graph showing the number of films released in certain years',
          fontsize=15)
plt.xticks(range(1925, 2022, 5))
plt.yticks(range(0, 1200, 50))
plt.legend(loc='upper left')
print(data)
