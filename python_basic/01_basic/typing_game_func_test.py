# 타자게임
# 데이터 저장 : word = []
# word  리스트에서 문제를 추출하여 제출하면 맞추는 게임
# - 한번 출제된 문제는 맞출때까지 반복
# - 전체 5문제를 출제 다 맞추면 종료


import json,time,random,sys

class TypingGame():

    def data_load(self,path):
        f = open(path,'r')
        data = json.load(f)
        f.close()
        return data

    def data_save(self,path,data):
        f = open(path,'w')
        json.dump(data,f)
        f.close()

    def game(self):
        print('게임시작!')
        start = time.time()
        n = 1
        quiz = random.choice(self.word)
        while n <= 5:
            print(f'{n}번')
            print(quiz)
            result = input('>>>')
            if quiz == result:
                print('통과!')
                n += 1
                quiz = random.choice(self.word)
            else:
                print('오타! 다시도전!')
        print('5문제 완료!!')
        end = time.time()
        print(f'걸린 시간 : {end-start:.0f}초')
        name = input('이름을 입력하세요 >>>')
        self.rank[name] = end-start
        print(self.rank)      

    def quiz_add(self):
        print('문제추가작업')
        while True:
            data = input('(종료:enter) >>>')
            if data == '':
                break
            self.word.append(data)
        print(self.word)

    def rank_list(self):
        print('등수리스트')
        for index,(k,v) in enumerate(sorted(self.rank.items(),key=lambda x : x[1])):
            print(f'{index+1}등 {k} 시간:{v:.0f}')

    def menu_display(self):
        menu_display = '''
        ------------------------------------------------------
        1.게임   2.문제추가  3.문제저장 4.등수리스트  5.종료
        ------------------------------------------------------
        >>> '''
        menu = input(menu_display)
        return menu

    def exe(self,menu):
        if menu == '1':
            self.game()  
        elif menu == '2':
            self.quiz_add()
        elif menu == '3':
            print('문제저장작업')
        elif menu =='4':
            self.rank_list()
        elif menu == '5':
            print('프로그램 종료!')
            self.data_save('python_basic/01_basic/word.josn',self.word)
            self.data_save('python_basic/01_basic/rank.josn',self.rank)
            sys.exit()
        else:
            print('메뉴를 선택하셨습니다.')

    def __init__(self):
        #self.word = self.data_load('python_basic/01_basic/word.josn')
        #self.rank = self.data_load('python_basic/01_basic/rank.josn')
        self.word = self.data_load('python_basic/01_basic/word.json')
        self.rank = self.data_load('python_basic/01_basic/rank.json')
        while True:
            self.exe(self.menu_display())

    #  H:\pythondata\python_basic\01_basic

TypingGame()