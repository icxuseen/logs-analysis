import psycopg2

# connect to database.
con = psycopg2.connect(
            host = "localhost",
            database = "news",
            user = "postgres",
            password = "1433"
)
#create a curser
cur = con.cursor()
# execute query
cur.execute("select title, name from articles join authors on articles.author = authors.id")

rows = cur.fetchall()
for r in rows:
    print(f"title {r[0]} name {r[1]}")


#close curser
cur.close()
# close the connection
con.close()

