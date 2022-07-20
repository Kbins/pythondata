# # 커피자판기
# 1. 커피자판기 2. 메뉴추가 3.메뉴삭제 4.메뉴목록 5.종료
# - 프로그램이 시작될때 필요한 정보를 읽어서 시작합니다.
# - 커피자판기 무한반복하면서 돈을 입력받고, 메뉴를 선택해서 처리
# - 메뉴추가 자판기에서 판매하는 메뉴를 추가하는 기능(메뉴명,가격)
# - 메뉴삭제는 전체 목록을 보여주고 삭제하고자하는 항목을 선택하도록 해서 삭제 처리
# - 메뉴목록은 메뉴이름순,메뉴가격순으로 정렬해서 보여줌.
# - 종료는 메뉴 정보를 저장하고 종료합니다.

item = {'아이스아메리카노':2000,
        '라떼':3500,
        '프라프치노':4500}
menu_display = '''
--------------------------------------------------------
1.커피자판기   2.메뉴추가  3.메뉴삭제  4.메뉴목록  5.종료
--------------------------------------------------------
>>> '''

while True:
    menu = input(menu_display)
    if menu == '1':
        choice = '선택한 메뉴'
        while choice:
            for k,v in item.items():
                print(f'{k}:{v:,}원',end=' ')
            print()
            choice = input('메뉴선택(종료:enter) >>>')
            money = int(input('금액 투입 >>>'))
            if choice in item.keys(): 
                if money >= item[choice]:
                    money -= item[choice]
                    print(f'{choice} 서비스 합니다. 거스름돈은 {money}')
            else:
                print('해당 메뉴가 없습니다.')                
            
    elif menu =='2':
        menu_name = input('메뉴명 >>> ')
        
        menu_price = ''
        while not menu_price.isdigit():
            menu_price = input('메뉴가격 >>> ')
        menu_price = int(menu_price)
        
        if menu_name in item.keys():
            print(f'{menu_name} 메뉴가 있습니다. 수정합니다. ')
        else:
            print(f'{menu_name} 메뉴를 추가합니다.')
        item[menu_name] = menu_price
        print(item)
    elif menu == '3':
        menu_name = input('삭제하려는 메뉴명 >>>')
        if menu_name in item.keys():
            print(f'{menu_name} 메뉴를 삭제합니다.')
            del item[menu_name]
        else:
            print(f'{menu_name} 메뉴가 없습니다.')
        print(item)            
    elif menu =='4':
        menu_1 = input('1.이름순 2.가격순 >>> ')
        if menu_1 == '1':
            for k,v in sorted(item.items(),key=lambda x : x[0]):
                print(f'{k:25} : {v:10,}원')
        elif menu_1 == '2':
            for k,v in sorted(item.items(),key=lambda x : x[1]):
                print(f'{k:25} : {v:10,}원')
    elif menu == '5':
        break
    else:
        print('메뉴를 잘못 선택하셨습니다.')