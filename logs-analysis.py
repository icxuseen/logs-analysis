#!/usr/bin/env python3
# import Postgresql library
import sys
import psycopg2
# import datetime.date module 
from datetime import date

DBNAME = "news"


def get_query_results(query):
    db = psycopg2.connect(
            host = "localhost",
            database = "news",
            user = "postgres",
            password = "1433")
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()




# Question 1: What are the most popular three articles of all time?
def get_top_articles():
    """Return the top three articles by most views"""
    query = """SELECT title, COUNT(log.id) AS views
            FROM articles, log
            WHERE log.path = CONCAT('/article/', articles.slug)
            GROUP BY articles.title ORDER BY views desc LIMIT 3;"""
    top_three = get_query_results(query)
    # Display header and results for Question 1
    print('**** Top Three Articles by Page View ****')
    for i in top_three:
        print('"' + i[0] + '" -- ' + str(i[1]) + " views")
    #print(" ")  # Display line break for legibility

# Question 2: Who are the most popular article authors of all time?
def get_top_authors():
    """Return the most popular authors based on overall page views"""
    query = """SELECT name, sum(articles_by_view.views) AS views
            FROM articles_by_author, articles_by_view
            WHERE articles_by_author.title = articles_by_view.title
            GROUP BY name ORDER BY views desc;"""
    author_popularity = get_query_results(query)
    # Display header and results for Question 2
    print('**** Most Popular Authors Based on Total Article Views ****')
    for i in author_popularity:
        print(i[0] + ' -- ' + str(i[1]) + ' views')
    #print(' ')  # Display line break for legibility

# Question 3: On which days did more than 1% of requests lead to errors?
def get_top_error_days():
    """Return the days where errors exceeded 1%"""
    query = """SELECT errors.day,
            ROUND(
            ((errors.errors/total.total) * 100)::DECIMAL, 2)::TEXT
            as percentage
            FROM errors, total
            WHERE total.day = errors.day
            AND (((errors.errors/total.total) * 100) > 1.0)
            ORDER BY errors.day;"""
    high_error_results = get_query_results(query)
    # Display header and results for Question 3
    print('**** Days Where Errors Exceeded 1%' + ' of Total Views ****')
    for i in high_error_results:
        print(i[0].strftime('%B %d, %Y') + " -- " + i[1] + "%" + " errors")
    #print(' ')  # Display line break for legibility


if __name__ == '__main__':
    get_top_articles()
    get_top_authors()
    get_top_error_days()


