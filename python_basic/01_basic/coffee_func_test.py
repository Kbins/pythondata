# # 커피자판기
# 1. 커피자판기 2. 메뉴추가 3.메뉴삭제 4.메뉴목록 5.종료
# - 프로그램이 시작될때 필요한 정보를 읽어서 시작합니다.
# - 커피자판기 무한반복하면서 돈을 입력받고, 메뉴를 선택해서 처리
# - 메뉴추가 자판기에서 판매하는 메뉴를 추가하는 기능(메뉴명,가격)
# - 메뉴삭제는 전체 목록을 보여주고 삭제하고자하는 항목을 선택하도록 해서 삭제 처리
# - 메뉴목록은 메뉴이름순,메뉴가격순으로 정렬해서 보여줌.
# - 종료는 메뉴 정보를 저장하고 종료합니다.

import sys,json

class Coffee: 
    def coffee_m(self):
        while True:
            for k,v in self.item.items():
                print(f'{k}:{v:,}원',end=' ')
            print()
            choice = input('메뉴선택(종료:enter) >>>')
            if choice =='':
                break
            money=''
            while not money.isdigit():
                money = input('금액 투입 >>>')
            money = int(money)

            if choice in self.item.keys(): 
                if money >= self.item[choice]:
                    money -= self.item[choice]
                    print(f'{choice} 서비스 합니다. 거스름돈은 {money}')
                else:
                    print('금액이 부족합니다.')
            else:
                print('해당 메뉴가 없습니다.')  

    def menu_add(self):
        menu_name = input('메뉴명 >>> ')
        menu_price = ''
        while not menu_price.isdigit():
            menu_price = input('메뉴가격 >>> ')
        menu_price = int(menu_price)
        
        if menu_name in self.item.keys():
            print(f'{menu_name} 메뉴가 있습니다. 수정합니다. ')
        else:
            print(f'{menu_name} 메뉴를 추가합니다.')
        self.item[menu_name] = menu_price
        print(self.item)

    def menu_del(self):
        menu_name = input('삭제하려는 메뉴명 >>>')
        if menu_name in self.item.keys():
            print(f'{menu_name} 메뉴를 삭제합니다.')
            del self.item[menu_name]
        else:
            print(f'{menu_name} 메뉴가 없습니다.')
        print(self.item)

    def menu_list(self):
        menu_1 = input('1.이름순 2.가격순 >>> ')
        if menu_1 == '1':
            for k,v in sorted(self.item.items(),key=lambda x : x[0]):
                print(f'{k:25} : {v:10,}원')
        elif menu_1 == '2':
            for k,v in sorted(self.item.items(),key=lambda x : x[1]):
                print(f'{k:25} : {v:10,}원')

    def data_load(self,path):
        f = open(path,'r')
        data = json.load(f)
        f.close()
        return data

    def data_save(self,path,data):
        f = open(path,'w')
        json.dump(data,f)
        f.close()

    def menu_display(self):
        menu_display = '''
--------------------------------------------------------
1.커피자판기   2.메뉴추가  3.메뉴삭제  4.메뉴목록  5.종료
--------------------------------------------------------
>>> '''

        menu = input(menu_display)
        return menu


    def exe(self,menu):
    
        if menu == '1':
            self.coffee_m()
        elif menu =='2':
            self.menu_add()
        elif menu == '3':
            self.menu_del()            
        elif menu =='4':
            self.menu_list()
        elif menu == '5':
            self.data_save('python_basic/01_basic/item.json',self.item)
            sys.exit()
        else:
            print('메뉴를 잘못 선택하셨습니다.')

    def __init__(self):
        self.item = self.data_load('python_basic/01_basic/item.json')
        while True:
            self.exe(self.menu_display())

Coffee() ## 클래스를 실행하면 된다