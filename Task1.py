import pandas as pd
import numpy as np
# a Create a dataframe, called movie_performance, with dc_marvel_movie_performance.csv data and check how data looks like
movie_performance = pd.read_csv("dc_marvel_movie_performance.csv")
# print(movie_performance.head())

# b Remove MCU, Phase and Franchise columns
movie_performance_new = movie_performance.drop(
    ['MCU', 'Phase', 'Franchise'], axis=1)
# print(movie_performance_new.head())

# c Find unique values of Character Family column and print them sorted from A to Z
unique_character_families = movie_performance_new['Character Family'].unique()
# print(sorted(unique_character_families))

# d Find the longest movie
longest_movie = movie_performance_new[[
    'Film', 'Minutes']].sort_values(by='Minutes', ascending=False)
# print(longest_movie.head(1))

# e Find mean values of “Rotten Tomatoes Critic Score” per “Break Even” categories
mean_score_per_break_even = movie_performance_new[[
    'Rotten Tomatoes Critic Score', 'Break Even']].groupby(['Break Even']).mean()
# print(mean_score_per_break_even.round(1))

# f Add a new column to movie_performance dataframe,  called “Recommended”, which takes value:

conditions = [
    (movie_performance_new['Rotten Tomatoes Critic Score'] > 90),
    (movie_performance_new['Rotten Tomatoes Critic Score'] <= 90) & (
        movie_performance_new['Rotten Tomatoes Critic Score'] >= 60),
    (movie_performance_new['Rotten Tomatoes Critic Score'] <= 59) & (
        movie_performance_new['Rotten Tomatoes Critic Score'] >= 40),
    (movie_performance_new['Rotten Tomatoes Critic Score'] < 40)
]

lables = ['Strongly yes', 'Yes', 'No', 'Strongly no']

movie_performance_new['Recommended'] = np.select(conditions, lables)
# print(movie_performance_new.head())

# g Create a new dataframe, called success_rate,  with success rateCreate a new dataframe, called success_rate,
# with success rate, that lists number of Flops and Successes for movies per Character Family, and calculates
# success rate (success rate = success/(success+flop) * 100%), so you should obtain something like that:

success_rate = movie_performance_new[['Film',
                                      'Character Family', 'Break Even']].copy()

success_rate['Flop'] = np.where(success_rate['Break Even'] == 'Flop', 1, 0)
success_rate['Success'] = np.where(
    success_rate['Break Even'] == 'Success', 1, 0)
success_rate_by_family = success_rate.groupby(
    ['Character Family']).sum(['Flop', 'Success'])
success_rate_by_family['Success Rate'] = (success_rate_by_family['Success'] / (
    success_rate_by_family['Success'] + success_rate_by_family['Flop']))*100
# Convert 'Success Rate' column to percentage values with 2 decimal places
success_rate_by_family['Success Rate'] = success_rate_by_family['Success Rate'].round(
    2)
success_rate_by_family['Success Rate'] = success_rate_by_family['Success Rate'].astype(
    str) + '%'
# print(success_rate_by_family)
# print(success_rate_by_family.dtypes)

# h Create a new dataframe, called directors, with directors.csv data and check how data looks like
directors = pd.read_csv("directors.csv")
# print(directors.head())

# i Print the result of joining movie_performance and directors dataframes, leaving only rows with Films that are present in
# both dataframes (you should get all the columns from movie_performance dataframe and column director from directors dataframe)
# in the movie_performance_new dataframem, there is no column 'Movie', but 'Film', rename the column name in the directors dataframe
directors.rename(columns={'Movie': 'Film'}, inplace=True)
# print(directors)
movies_and_directors = directors.merge(
    movie_performance_new, how='left', on='Film')
print(movies_and_directors)
