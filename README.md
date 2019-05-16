# Log Analysis Project
## Udacity Full Stack Nanodegree

### Project Overview
This reporting tool is a Python program using the `psycopg2` module to connect to the database.

### questions
The reporting tool needed to answer the following questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

### How to Run the Code
This section will describe the SQL views I created for the code to function properly and how to run the program.

#### Required SQL Views
This program uses four SQL views.

**For Question 2:**

> `CREATE VIEW articles_by_author AS
SELECT title, name
FROM articles, authors
WHERE articles.author = authors.id;`

> `CREATE VIEW articles_by_view AS
SELECT articles.title, COUNT(log.id) AS views
FROM articles, log
WHERE log.path = CONCAT('/articles/', articles.slug)
GROUP BY articles.title
ORDER BY views desc;`

**For Question 3:**

>`CREATE VIEW errors AS
SELECT DATE(time) as day, CAST(COUNT(status) AS FLOAT) AS errors
FROM log
WHERE NOT status='200 OK'
GROUP BY day
ORDER BY day;`

>`CREATE VIEW total AS
SELECT DATE(time) AS day, CAST(COUNT(status) AS FLOAT) AS total
FROM log
GROUP BY day
ORDER BY day;`

#### Running the Program
 

First, you'll need to create the views listed above:
1. Install PostgreSQL`
2. Run PostgreSQL to Connect to the database`
3. Import  `news.sql file`
4. Create the views listed above
5. Execute the file logs-analysis.py