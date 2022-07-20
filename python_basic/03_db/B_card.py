#명함관리 프로그램
# - 명함등록 (일련번호(중복X),이름,전화번호,email,회사명)
# - 명함수정
# - 명함삭제
# - 리스트 출력
# - 종료

import sqlite3, sys, re

class B_Card():
    
    def b_card(self):
        menu_display = input('''
    --------------------------------------------------
    1.명함 등록 2.명함 수정 3.명함 삭제 4.리스트 출력 5.종료
    --------------------------------------------------
    ''')

        #조건문 작성
        if menu_display =='1':
            self.create()
            self.insert()
        elif menu_display =='2':
            self.update()
        elif menu_display =='3':
            self.delete()
        elif menu_display =='4':
            self.select()
        elif menu_display =='5':
            sys.exe()
            print('종료')
        else:
            print('다시 입력해주세요')

    #----------------------------------------------------------------
    
    def __init__(self):
        while True:
            self.b_card()

    #생성
    def create(self):
        conn = sqlite3.connect('python_basic/03_db/B_card.db')
        cur = conn.cursor()
        cur.execute('''
        create table if not exists B_card(
            idx  integer,
            name text,
            tel  text,
            mail text,
            com  text
        )
        ''')

        conn.commit()
        conn.close()

    #생성
    def insert(self):
            print('명함등록')
            conn = sqlite3.connect('python_basic/03_db/B_card.db')
            cur = conn.cursor()

            sql = 'select idx, name, tel, mail, com from B_card order by idx asc'
            cur.execute(sql)
            for i in cur.fetchall():
                print(i)
            try:
                idx  = int(input('인덱스 입력 :'))
            except:
                print('정수만 허용!')
                idx  = int(input('인덱스 입력 :'))

            name = input('이름 입력 :')
            tel  = input('전화번호 입력 :')

            # p = re.compile('[a-z][a-z0-9]{4,}@[a-z]{2,}[.](kr|com|org|net)$')
            # mail = input('메일 입력 :')
            # result = p.match(mail)

            mail = input('메일 입력 :')
            com  = input('회사명 입력 :')

            data = (idx, name, tel, mail, com)
            sql = 'insert into B_card values(:1,:2,:3,:4,:5)'
            cur.execute(sql,data)
            conn.commit()
            print(f'추가: {data}')
            conn.close()


    #수정
    def update(self):
            print('명함수정')
            conn = sqlite3.connect('python_basic/03_db/B_card.db')
            cur = conn.cursor()
            
            sql = 'select idx, name, tel, mail, com from B_card order by idx asc'
            cur.execute(sql)
            data = cur.fetchall()
            for i in data:
                print(i)
            try:
                idx = int(input('수정할 idx :'))
            except:
                print('정수를 입력하세요!')
                idx = int(input('수정할 idx :'))

            col = input('수정할 컬럼(name, mail, tel, com) :')
            values = input('수정할 내용 :')
        
            sql = f'update B_card set {col} = ? where idx = ?'
            cur.execute(sql,(values,idx))
            # cur.fetchall()
            conn.commit()
            print(f'수정: 인덱스{idx}의 {values} ')
            #print(f'{data}!!!! ')
            conn.close()

    #삭제
    def delete(self):
            print('명함삭제')
            conn = sqlite3.connect('python_basic/03_db/B_card.db')
            cur = conn.cursor()

            sql = 'select idx,name,tel,mail,com from B_card'
            cur.execute(sql)
            data = cur.fetchall()
            for i in data:
                print(i)

            values = input('삭제할 내용 :')
            col = input('삭제할 컬럼 조건 :')

            
            # if values in cur.fetchall():
            # sql = f'delete from B_card where {col} like ? ' 아닌가?
            # cur.execute(sql,(f'%"+{values}+"%',))

            sql = f'delete from B_card where {col} like "%" || ? || "%" '
            cur.execute(sql,(values,))
            # sql = f'delete from B_card where idx = {col}'
            # cur.execute(sql)
            conn.commit()
            print(f'{values}의 행 삭제완료')
            print(data)
            conn.close()

    #리스트 조회
    def select(self):
            conn = sqlite3.connect('python_basic/03_db/B_card.db')
            cur = conn.cursor()
            choice = input('1.이름순 , 2.index순')

            if choice =='1':
                sql = 'select idx, name, tel, mail, com from B_card order by name asc'
            elif choice =='2':
                sql = 'select idx, name, tel, mail, com from B_card order by idx asc'
            else:
                print('다시 입력하세요')
            cur.execute(sql)
            data = cur.fetchall()
            conn.close()
            print(data)

B_Card()