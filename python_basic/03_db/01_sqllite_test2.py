import sqlite3

from sympy import symbols

conn = sqlite3.connect('python_basic/03_db/example.db')
cur = conn.cursor()

symbol = 'RHAT'
cur.execute('select * from stocks')
data = cur.fetchall()
for item in data:
    print(item)
# 커밋이 없음 변경사항이 없기떄문에
conn.close()