# Importing libraries and configuration file
import os
import glob
# import numpy as np
import pandas as pd

dataset_path = './'
articles_path = glob.glob(os.path.join(dataset_path, "News Articles/*/*.txt"))
summaries_path = glob.glob(os.path.join(dataset_path, "Summaries/*/*.txt"))


articles_path.sort()
summaries_path.sort()

print(articles_path[:5])
print(summaries_path[:5])


# Loading the data into arrays
articles = []
summaries = []

for article_path, summary_path in zip(articles_path, summaries_path):
    with open(article_path, "r", encoding="ISO-8859-1") as article_file:
        article_text = article_file.read()
        articles.append(article_text)

    with open(summary_path, "r", encoding="ISO-8859-1") as summary_file:
        summary_text = summary_file.read()
        summaries.append(summary_text)


categories_list = os.listdir(os.path.join(dataset_path, 'News Articles'))
categories = []
def print_file_data():
    for category in categories_list:
        article_paths = glob.glob(os.path.join(dataset_path, "News Articles", category, "*.txt"))
        summary_paths = glob.glob(os.path.join(dataset_path, "Summaries", category, "*.txt"))

        for i in article_paths:
            categories.append(category)

        if len(article_paths) != len(summary_paths):
            print("Length of dataset not equal for subdirectory :", category)
        else:
            print(f"Found {len(article_paths)} articles and {len(summary_paths)} summaries in the subdirectory : {category}")

print_file_data()


# Creating pandas dataframe
df = pd.DataFrame({
    'Articles' : articles,
    'Summaries' : summaries,
    'Categories' : categories
})

print(df.head())

df.to_csv("BBC_news_dataset.csv", index=False)
