# Logs Analysis Project

1. psql news (this will access the "news" database found in newsdata.sql).

2. The articles,logs and author tables are successfully dropped.

3. Then in the shell, re-import the data: psql -h localhost -U postgres -p 5432 news < newsdata.dump

4. connect the two tables with a join.

