import sqlite3

conn = sqlite3.connect('python_basic/03_db/example.db')
cur = conn.cursor()

data = [('2006-03-28', 'BUY', 'IBM', 300.0, 45.14),
        ('2006-04-05', 'BUY', 'MSFT', 1000.0, 76.00),
        ('2006-05-06', 'BUY', 'IBM', 500.0, 290.14)]
sql = 'insert into stocks values(?,?,?,?,?)'

#symbol = 'RHAT'
cur.executemany(sql,data)
conn.commit()
conn.close()