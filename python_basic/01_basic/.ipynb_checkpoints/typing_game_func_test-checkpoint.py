# 타자게임
# 데이터 저장 : word = []
# word리스트에서 문제를 추출하여 제출하면 맞추는 게임
# - 한 번 출제된 문제는 맞출때까지 반복
# - 전체 5문제를 출제 다 맞추면 반복

import json,time
f = open('word.json','r')
word = json.load(f)
f.close()
# word=[]
rank={'강동근': 11.932971954345703, '정병윤': 12.767038583755493}

menu_display = '''
-----------------------------------------------------
1.게임 2.문제추가 3.문제저장 4.등수리스트 5.종료
-----------------------------------------------------
>>>'''

import tyoing_game_func as tgf
import os
 path = os.path.word()
while True:
    menu = input(menu_display)
    if menu == '1':
        print('게임시작')

        
    elif menu == '2':
        print('문제추가작업')

            
    elif menu =='3':
        print('문제저장작업')
         
        
    elif menu =='4':
        print('등수리스트')

        
    elif menu =='5':
        print('프로그램종료!')

    else:
        print('메뉴를 선택하셨습니다')