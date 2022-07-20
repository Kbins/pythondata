import cx_Oracle

#print(cx_Oracle.version)

# conn = cx_Oracle.connect('auth/1@localhost:1521/xe')
# cur = conn.cursor()
# data = ('AUTH009','삭제권한')
# sql = 'insert into authes values(:1,:2)'
# cur.execute(sql,data)
# conn.commit()
# sql = 'select * from authes'
# cur.execute(sql)
# data = cur.fetchall()
# for item in data:
#     print(item)
# conn.close()

#명함관리 프로그램
# - 명함등록 (일련번호(중복X),이름,전화번호,email,회사명)
# - 명함수정
# - 명함삭제
# - 리스트 출력
# - 종료


conn = cx_Oracle.connect('auth/1@localhost:1521/xe')
cur = conn.cursor()

data1 = input('인덱스')
data2 = input('이름 입력')
data3 = input('전화변호 입력')
data4 = input('메일 입력')
data5 = input('회사명 입력')

data = (data1,data2,data3,data4,data5)
sql = 'insert into B_card values(:1,:2,:3,:4,:5)'
cur.execute(sql,data)
conn.commit()
print(data)

sql = 'select * from B_card'
cur.execute(sql)
data = cur.fetchall()
conn.close()
print(data)
