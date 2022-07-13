import pandas as pd
import matplotlib.pyplot as plt


def create_data_frame():
    """This function will create DataFrame from CSV file using Pandas"""
    return pd.read_csv('netflix_titles.csv', delimiter=',',
                       usecols=['release_year']).value_counts().to_frame()\
        .sort_values(by='release_year').reset_index().rename(
        columns={'release_year': 'Release Year', 0: 'Amount'})


def create_chart(data):
    """This function will create the chart showing amount of movies released
    in certain year using Matplotlib"""
    data.plot(x='Release Year', y='Amount', rot=90, figsize=(15, 10),
              grid=True, color='red')
    plt.xlabel('Release Year', fontsize=15)
    plt.ylabel('Amount of released movies', fontsize=15)
    plt.title('Chart showing the number of films released in certain years',
              fontsize=15)
    plt.xticks(range(1925, 2022, 5))
    plt.yticks(range(0, 1200, 50))
    plt.legend(loc='upper left')
    return plt.show()


print(create_data_frame())
create_chart(create_data_frame())
