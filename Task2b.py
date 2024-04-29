# Data Visualisations
# Please create a pie chart, displaying the portion of films falling into each of “Recommended” column categories
# (or, alternatively of “MPAA Rating” column, if you have not completed task 1f) )
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

movie_performance = pd.read_csv("dc_marvel_movie_performance.csv")
movie_performance_new = movie_performance.drop(
    ['MCU', 'Phase', 'Franchise'], axis=1)

# adding 'Recommended' column
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

# pie chart pandas and matplotlib
pie_data = movie_performance_new['Recommended'].value_counts()
pie_data.plot(kind='pie', labels=pie_data.index,
              autopct='%1.1f%%', startangle=140)


plt.title('Distribution of Films by "Recommended" Category')
plt.ylabel('')  # Remove y-axis label (y axis says 'count')

plt.show()
