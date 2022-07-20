import sqlite3

conn = sqlite3.connect('python_basic/03_db/example.db')
cur = conn.cursor()

sql = 'select * from stocks order by price desc'

cur.execute(sql)

data = cur.fetchall()
for i in data:
        print(i)
conn.close()