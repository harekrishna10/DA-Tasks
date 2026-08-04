# PANDAS DATA MANIPULATION ASSIGNMENT
# Dataset: Netflix Movies and TV Shows Dataset
# 1. Load the dataset using Pandas.
import pandas as pd
netflix_movies_and_TV_shows = pd.read_csv('Netflix Movies and TV Shows.csv')
print(netflix_movies_and_TV_shows)

# 2. Display the first 10 rows of the dataset.
print(netflix_movies_and_TV_shows.head(10))


# 3. Display the last 5 rows of the dataset.
print(netflix_movies_and_TV_shows.tail())


# 4. Find the total number of rows and columns.
print(netflix_movies_and_TV_shows.shape)


# 5. Display all column names.
print(netflix_movies_and_TV_shows.columns)


# 6. Check the data types of all columns.
print(netflix_movies_and_TV_shows[netflix_movies_and_TV_shows.columns].dtypes)


# 7. Find the total number of missing values in each column.
print(netflix_movies_and_TV_shows.isna().sum())


# 8. Find the total number of duplicate rows.
print(netflix_movies_and_TV_shows.duplicated().sum())


# 9. Remove duplicate rows from the dataset.
netflix_movies_and_TV_shows = netflix_movies_and_TV_shows.drop_duplicates()
print(netflix_movies_and_TV_shows)


# 10. Replace missing values in the director column with "Unknown".
netflix_movies_and_TV_shows['director'] = netflix_movies_and_TV_shows['director'].fillna('Unknown')
print(netflix_movies_and_TV_shows)


# 11. Convert the date_added column into datetime format.
netflix_movies_and_TV_shows = pd.read_csv('Netflix Movies and TV Shows.csv', parse_dates=['date_added'], date_format='%B %d, %Y')
print(netflix_movies_and_TV_shows[['title', 'date_added']].head())


# 12. Find the total number of Movies and TV Shows.
total_movies_and_TV_Shows_count = netflix_movies_and_TV_shows['type'].value_counts()
print(total_movies_and_TV_Shows_count)


# 13. Display only Movies from the dataset.
only_movies_display = netflix_movies_and_TV_shows[netflix_movies_and_TV_shows['type'] == 'Movie']
print(only_movies_display)


# 14. Display only TV Shows from the dataset.
only_TV_Shows_display = netflix_movies_and_TV_shows[netflix_movies_and_TV_shows['type'] == 'TV Show']
print(only_TV_Shows_display)


# 15. Find all content released after 2018.
content_after_2018 = netflix_movies_and_TV_shows[netflix_movies_and_TV_shows['release_year'] > 2018]
print(content_after_2018[['title','type','release_year']])


# 16. Find all content produced in India.
contenct_prod_in_india = netflix_movies_and_TV_shows[netflix_movies_and_TV_shows['country'] == 'India']
print(contenct_prod_in_india[['title','type','release_year','country']])


# 17. Find all content produced in the United States.
contenct_prod_in_united_state = netflix_movies_and_TV_shows[netflix_movies_and_TV_shows['country'] == 'United States']
print(contenct_prod_in_united_state[['title','type','release_year','country']])


# 18. Find all movies with rating "PG-13".
movie_rating_PG13 = netflix_movies_and_TV_shows[netflix_movies_and_TV_shows['rating'] == 'PG-13']
print(movie_rating_PG13[['title','type','release_year','country','rating']])


# 19. Find the top 10 countries with the highest Netflix content.
top_10_netflix_ctry = netflix_movies_and_TV_shows['country'].value_counts().head(10)
print(top_10_netflix_ctry)


# 20. Find the most common rating in the dataset.
most_common_rating = netflix_movies_and_TV_shows['rating'].value_counts().idxmax()
rating_ra_title = netflix_movies_and_TV_shows[netflix_movies_and_TV_shows['rating'] == most_common_rating]
print(rating_ra_title[['title','rating']])


# 21. Find the oldest movie/show in the dataset.
oldest_movie_show = netflix_movies_and_TV_shows[netflix_movies_and_TV_shows['release_year'] == netflix_movies_and_TV_shows['release_year'].min()]
print(oldest_movie_show[['title','type','release_year']])


# 22. Find the newest movie/show in the dataset.
newest_movie_show = netflix_movies_and_TV_shows[netflix_movies_and_TV_shows['release_year'] == netflix_movies_and_TV_shows['release_year'].max()].head(1)
print(newest_movie_show[['title','type','release_year']])


# 23. Find all titles containing the word "Love".
title_with_love = netflix_movies_and_TV_shows[netflix_movies_and_TV_shows['title'].str.contains('love',case=False,na=False)]
print(title_with_love[['title','type','release_year']])


# 24. Find all titles containing the word "Crime".
title_with_crime = netflix_movies_and_TV_shows[netflix_movies_and_TV_shows['title'].str.contains('Crime',case=False,na=False)]
print(title_with_crime[['title','type','release_year']])


# 25. Find all content where Adam Sandler is part of the cast.
cast_with_Adam_Sandler = netflix_movies_and_TV_shows[netflix_movies_and_TV_shows['cast'].str.contains('Adam Sandler',case=False,na=False)]
print(cast_with_Adam_Sandler[['title','type','cast','release_year']])


# 26. Count how many contents belong to the "Documentaries" genre.
number_of_documnetaries = netflix_movies_and_TV_shows[netflix_movies_and_TV_shows['listed_in'].str.contains('Documentaries',case=False,na=False)]
total_number_of_documentaries = len(number_of_documnetaries)
print("Total content with documentaries are:",total_number_of_documentaries)


# 27. Count how many contents belong to the "Comedies" genre.
number_of_comedies = netflix_movies_and_TV_shows[netflix_movies_and_TV_shows['listed_in'].str.contains('Comedies',case=False,na=False)]
total_number_of_comedies = len(number_of_comedies)
print("Total content with comedies are:",total_number_of_comedies)


# 28. Create a new column named content_age using:
#     content_age = 2026 - release_year
netflix_movies_and_TV_shows['content_age'] = 2026 - netflix_movies_and_TV_shows['release_year']
print(netflix_movies_and_TV_shows[['title','type','release_year','content_age']].head())


# 29. Find the movie with the longest duration.
movies_from_type = netflix_movies_and_TV_shows[netflix_movies_and_TV_shows['type'] == 'Movie']
longest_duration_movies = movies_from_type['duration'].idxmax()
print(movies_from_type.loc[longest_duration_movies,['title','type','release_year','duration']])


# 30. Find the TV Show with the highest number of seasons.
TV_Shows_from_type = netflix_movies_and_TV_shows[netflix_movies_and_TV_shows['type'] == 'TV Show']
highest_season_TV_Shows = TV_Shows_from_type['duration'].idxmax()
print(TV_Shows_from_type.loc[highest_season_TV_Shows,['title','type','release_year','duration']])


# 31. Extract only the numeric value from the duration column.
netflix_movies_and_TV_shows['duration_numeric_value'] = (netflix_movies_and_TV_shows['duration'].str.extract(r'(\d+)')[0].astype('Int64'))
print(netflix_movies_and_TV_shows[['duration', 'duration_numeric_value']])


# 32. Find the number of contents added each year.
number_of_content_yearly = netflix_movies_and_TV_shows['release_year'].value_counts()
print(number_of_content_yearly)


# 33. Create separate DataFrames for Movies and TV Shows.
movies_dataframe = netflix_movies_and_TV_shows[netflix_movies_and_TV_shows['type'] == 'Movie']
TV_Shows_dataframe = netflix_movies_and_TV_shows[netflix_movies_and_TV_shows['type'] == 'TV Show']
print("Movies Dataframe:",movies_dataframe)
print("Tv Shows Dataframe:",TV_Shows_dataframe)


# 34. Find the top 10 directors with the highest number of contents.
top_10_directors = netflix_movies_and_TV_shows['director'].value_counts().head(10)
print("Top 10 Directors:",top_10_directors)


# 35. Create a pivot table showing average release year by type.
pivot_table = netflix_movies_and_TV_shows.pivot_table(values='release_year',index='type',aggfunc='mean')
print("Pivot Table by Type showing Average release year: \n",pivot_table)


# 36. Sort the dataset by release_year in descending order.
dataset_by_type_in_descendingorder = netflix_movies_and_TV_shows.sort_values(by='release_year',ascending=False)
print(dataset_by_type_in_descendingorder[['title','release_year']])


# 37. Find all content added after 2020.
content_after_2020 = netflix_movies_and_TV_shows[netflix_movies_and_TV_shows['release_year'] > 2020]
print(content_after_2020[['title','type','release_year','date_added']])

# 38. Find all TV Shows with more than 3 seasons.
TV_shows_more_than_3shows = netflix_movies_and_TV_shows[(netflix_movies_and_TV_shows['type'] == 'TV Show') & (netflix_movies_and_TV_shows['duration_numeric_value'] > 3)]
print(TV_shows_more_than_3shows[['title','type','duration','duration_numeric_value']])


# 39. Find the number of unique ratings available in the dataset.
total_number_of_unique_rating = netflix_movies_and_TV_shows['rating'].nunique()
print("Total number of Unique rating are:",total_number_of_unique_rating)


# 40. Write 5 interesting insights you discovered from the dataset.
#1) Netflix releases more TV Shows after 2020.
#2) Not all TV Shows are completed or more than 2 seasons are released.
#3) Netflix got increment in viewers during pandamic.
#4) Majority of netflix viewers gave TV-MA rating.
#5) Regional directors are dominating mainstream directors.