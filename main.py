"""
Project name: Netflix data Analysis
Created by: Prakhar Tripathi and Ishita Mishra
Description: There is a dataset in the form of CSV formate and, we have to perform some EDA (Exploratory data analysis)
by which we find some insights and also solving the problems related to this analysis.
"""

# Importing the packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
# importing the dataset
df = pd.read_csv("C:\\Users\\prakh\\Downloads\\Pycharm Projects\\Netflix data analysis\\data\\Netflix Dataset.csv")
print(df)
# Checking the columns name
print(df.columns)

# Top 10 data of dataset
print(df.head(10))

# Last 10 data of dataset
print(df.tail(10))

# Checking Null Values
print(df.info())

# Statical Analysis
print(df.describe())

# Fetching the year from releasing date
df["Releasing_Year"] = pd.DatetimeIndex(df["Release_Date"]).year
print(df["Releasing_Year"])

# Fetching the month from releasing date
df["Releasing_month"] = pd.DatetimeIndex(df["Release_Date"]).month
df["Releasing_month"] = pd.to_datetime(df["Releasing_month"], format="%m").dt.month_name()
print(df["Releasing_month"])

# EDA(Exploratory data analysis)

# Category of Netflix shows
print(df["Category"].value_counts())

# Top 5 directors who create maximum shows
print(df["Director"].value_counts()[:5])

# Top 5 cast who get maximum movies
print(df["Cast"].value_counts()[:5])

# Top 5 country with maximum shows
print(df["Country"].value_counts()[:5])

# Countries which have maximum movies
movie_df = df[df["Category"] == "Movie"]
print(movie_df["Country"].value_counts()[:5])

# Top 5 Country in which Raúl Campos, Jan Suter direct the movie
director_df = movie_df[movie_df["Director"] == "Raúl Campos, Jan Suter"]
print(director_df["Country"].value_counts()[:5])

# Rating for Raul Campos
print(director_df["Rating"].value_counts())

# Top 5 Movies On Netflix
print(movie_df["Title"].value_counts()[:5])

# Top 5 Netflix movies and shows
print(df["Title"].value_counts()[:5])

# Top 5 Releasing years
print(df["Releasing_Year"].value_counts().head())

Year_df = df[df["Releasing_Year"] == 2019]

# Top 5 countries with max Netflix shows in 2019

print(Year_df["Country"].value_counts()[:5])

# Top 5 directors with max Netflix shows in 2019
print(Year_df["Director"].value_counts()[:5])

# Top category with max Netflix shows in 2019
print(Year_df["Category"].value_counts())

# Count of ratings
print(df["Rating"].value_counts())

# Count of releasing month
print(df["Releasing_month"].value_counts())

# Top 5 Count of Types of shows on netflix
print(df["Type"].value_counts()[:5])

# Documentary Dataset
documentary_df = df[df["Type"] == "Documentaries"]

# Top 5 directors who direct documentary
print(documentary_df["Director"].value_counts()[:5])

# Print the id and director of house of cards
h_o_c_df = df[df["Title"] == "House of Cards"]
print(h_o_c_df[["Show_Id", "Director"]])

# Top 5 TV Shows exclusive in india
shows_df = df[df["Category"] == "TV Show"]
country_df = shows_df[shows_df["Country"] == "India"]
print(country_df["Title"].value_counts()[:5])

# Country with maximum shows
print(shows_df["Country"].value_counts()[:5])

# Data sorted by releasing year
print(df.sort_values(by=["Releasing_Year"]))

# Visualization Task
#
# # Category count
# plt.figure(figsize=(8, 16))
# category = ["Movie", "TV Show"]
# value = df["Category"].value_counts()
# plt.bar(category, value, color="grey")
# plt.title("Category Count")
# plt.xlabel("Category")
# plt.ylabel("Counts")
# plt.show()
#
# # Top Director count
# plt.figure(figsize=(10, 7))
# plt.title('Top 5 Directors on Netflix Shows')
# director = df["Director"].value_counts()[:5]
# plt.pie(director, autopct='%.2f', labels=director.index)
# plt.show()
#
# # Top Cast count
# plt.figure(figsize=(10, 7))
# plt.title('Top 5 cast on Netflix Shows')
# cast = df["Cast"].value_counts()[:5]
# plt.pie(cast, autopct='%.2f', labels=cast.index)
# plt.show()
#
# # Top 5 Countries
# plt.figure(figsize=(10, 7))
# plt.title("Top 5 Countries")
# top_countries = df["Country"].value_counts()[:5]
# sns.barplot(x=top_countries.index, y=top_countries.values)
# plt.show()
#
# # Top 5 Countries where maximum movies launched
# plt.figure(figsize=(10, 7))
# plt.title("Top 5 Countries where maximum movies launched")
# top_countries = movie_df["Country"].value_counts()[:5]
# sns.barplot(x=top_countries.index, y=top_countries.values, color="skyblue")
# plt.show()
#
# # Top 5 Country in which Raúl Campos, Jan Suter direct the movie
# plt.figure(figsize=(10, 7))
# plt.title('Top 5 Country in which Raúl Campos, Jan Suter direct the movie')
# direct = director_df["Country"].value_counts()[:5]
# plt.pie(direct, autopct='%.2f', labels=direct.index)
# plt.show()
#
# # Rating of raul Campos movies on netflix
# plt.figure(figsize=(10, 7))
# plt.title("Rating of Raul Campos movies on netflix")
# rating = director_df["Rating"].value_counts()
# sns.barplot(x=rating.index, y=rating.values, color="orange")
# plt.show()

# Top 5 movies on netflix
# plt.figure(figsize=(10, 7))
# plt.title('Top 5 movies and TV shows on Netflix')
# movie =df["Title"].value_counts()[:5]
# plt.pie(movie, autopct='%.2f', labels=movie.index, colors=["skyblue", "orange", "green", "purple", "yellow"])
# plt.show()

# Top 5 years in which netflix releases most
# plt.figure(figsize=(10, 7))
# plt.title("Top 5 years in which netflix releases most")
# years = df["Releasing_Year"].value_counts().head()
# sns.barplot(x=years.index, y=years.values, color="silver")
# plt.show()

# Months in which netflix releases most
# plt.figure(figsize=(10, 7))
# plt.title("Months in which netflix releases most")
# month = df["Releasing_month"].value_counts()
# sns.barplot(x=month.index, y=month.values, color="blue")
# plt.show()

# Count of ratings
# plt.figure(figsize=(10, 7))
# plt.title("Count of ratings")
# count_rating = df["Rating"].value_counts()
# sns.barplot(x=count_rating.index, y=count_rating.values, color="lightgreen")
# plt.show()

# Top 5 Types of shows on netflix
plt.figure(figsize=(5, 3))
plt.title("Top 5 Types of shows on netflix")
label=["Documentry", "Stand-up", "Drama", "International Movies", "Independent Movies"]
type = df["Type"].value_counts()[:5]
sns.barplot(x=label, y=type.values, color="pink")
plt.show()



