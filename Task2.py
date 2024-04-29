# Data Visualisation
# a Please find top 5 films in movie_performance dataframe with highest "Gross to Budget" value (earning ratio)
# and create a bar plot that shows film names on the x-axis and “Gross to Budget” on the y-axis (this example should help:
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_colors.html#sphx-glr-gallery-lines-bars-and-markers-bar-colors-py)
import pandas as pd
import matplotlib.pyplot as plt

movie_performance = pd.read_csv("dc_marvel_movie_performance.csv")

# movies with the highest "Gross to budget" value
top_gross_to_budget_movies = movie_performance[[
    'Gross to Budget', 'Film']].sort_values(by='Gross to Budget', ascending=False)
# print(top_gross_to_budget_movies)
top_5_gross_to_budget_movies = top_gross_to_budget_movies.head(5)
# print(top_5_gross_to_budget_movies)

# bar plot
fig, ax = plt.subplots()
movies = top_5_gross_to_budget_movies['Film']
gross_to_budget = top_5_gross_to_budget_movies['Gross to Budget']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:green', 'tab:orange']

ax.bar(movies, gross_to_budget, color=bar_colors)

ax.set_ylabel('Gross to budget (earning ratio)')
ax.set_xlabel('Movies')
ax.set_title('Top 5 movies per earning ratio')

# adjust the x labels
plt.xticks(rotation=45, ha='right')
# adjust layout to prevent label overlap
plt.tight_layout()

plt.show()
