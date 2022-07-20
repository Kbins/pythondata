from distutils.util import execute
import sqlite3

from matplotlib.pyplot import title


def create_table():
    conn = sqlite3.connect('python_basic/03_db/my_book.db')
    cur = conn.cursor()
    cur.execute('''
    create table if not exists books(
        title text,
        published_date text,
        pulisher text,
        pages integer,
        recommend integer
    )
    ''')
    conn.commit()
    conn.close()

def insert_book():
    #책이름,출판일자,출판사,페이지 수, 추천
    conn = sqlite3.connect('python_basic/03_db/my_book.db')
    cur = conn.cursor()

    title = input('책이름 >> ')
    date = input('출판일자 >> ')
    publisher = input('출판사 >> ')
    pages = input('총 페이지 수 >> ')
    recommend = input('추천 수 >> ')
    data = [title,date,publisher,pages,recommend]
    sql = 'insert into books values(?,?,?,?,?)'
    cur.execute(sql,data)
    conn.commit()
    conn.close()

def list_book():
    conn = sqlite3.connect('python_basic/03_db/my_book.db')
    cur = conn.cursor()
    cur.execute('select * from books')
    data = cur.fetchall()
    for item in data:
        print(f'책제목:{item[0]} 출판일자:{item[1]} 출판사:{item[2]} 총페이지:{item[3]} 추천수:{item[4]}')
    conn.close()

def update_book():
    conn = sqlite3.connect('python_basic/03_db/my_book.db')
    cur = conn.cursor()
    title = input('수정할 책 제목 -->')
    col = input('수정할 항목 -->')
    value = input('수정할 내용 -->')
    sql = f'update books set ? = {col}  where title = ?'
    cur.execute(sql,(value,title))
    conn.commit()
    conn.close()

def delete_book():
    conn = sqlite3.connect('python_basic/03_db/my_book.db')
    cur = conn.cursor()

    col = input('삭제할 조건 컬럼 -->')
    value = input('삭제할 조건 -->')
    sql = f'delete from books where {col} like ?'
    result = cur.execute(sql,('%'+value+'%'))
    print(result)
    conn.commit()
    conn.close()

    # title = input('삭제할 책 제목 -->')
    # if title in f'select * from books':
    #     print('존재')
    # else:
    #     sql = f'delete from books where title = ?'
    # print('삭제완료')

