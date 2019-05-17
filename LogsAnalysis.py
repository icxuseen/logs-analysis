#!/usr/bin/env python3
# -*- encoding: utf-8 -*-       # Use if python2
import sys
import psycopg2

DBNAME = "news"

def ExecuteQuery(query):
    db = psycopg2.connect(host = "localhost",database = ""+ DBNAME +"",user = "postgres",password = "1433")
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()

def answer1():
    print("Question 1: What are the most popular three articles of all time?\n")
    
    query = """SELECT title, COUNT(log.id) AS views
                FROM articles
                JOIN log ON log.path = CONCAT('/article/', articles.slug)
                GROUP BY articles.title ORDER BY views desc LIMIT 3;"""
                            
    QueryAnswer1 = ExecuteQuery(query)
    
     #"""Answer the first question ..."""
    print('**** Answer the first question ****')
    for i in QueryAnswer1:
        print('"' + i[0] + '" -- ' + str(i[1]) + " views")

def answer2():
  
    print("Question 2: Who are the most popular article authors of all time?\n")

    query = """SELECT authors.name, COUNT(log.id) AS CountViews FROM authors
            LEFT JOIN articles on articles.author = authors.id
            LEFT JOIN log on log.path = ('/article/' || articles.slug)
            GROUP BY
            authors.name ORDER BY CountViews desc"""
                            
    QueryAnswer2 = ExecuteQuery(query)

    # """Answer second question ..."""
    print('**** Answer second question ****')
    for i in QueryAnswer2:
        print('"' + i[0] + '" -- ' + str(i[1]) + " views")

def answer3():
   # """Answer the third first question ..."""
    print("Question 3: On which days did more than 1% of requests lead to errors??\n")
  
    query = """SELECT
            TO_CHAR(errors_day.date,'Month DD, YYYY') AS date,
            TO_CHAR(((errors_day.count::decimal
                    /requests_day.count::decimal)*100)
                    ,'9.99')
                    || '%' AS percentage
        FROM
            (SELECT date(time),COUNT(*) FROM log
                        group by date(time)) as requests_day,
            (SELECT date(time),count(*) FROM log where status != '200 OK'
                        group by date(time)) as errors_day
        WHERE
            requests_day.date = errors_day.date
            and ((errors_day.count::decimal
                    /requests_day.count::decimal)*100) > 1;"""
                            
    QueryAnswer3 = ExecuteQuery(query)

    # """Answer the third first question ..."""
    print('**** Answer the third first question ****')
    for i in QueryAnswer3:
        print('"' + i[0] + '" -- ' + str(i[1]) + " Errors")

def run():
   # """Running report ..."""
    print("Running reporting tools...\n")
    answer1()
    print("\n")

    answer2()
    print("\n")

    answer3()
    print("\n")

if __name__ == '__main__':
    run()
