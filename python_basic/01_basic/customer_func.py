import json, re

def data_load(path):
    f = open(path,'r')
    data = json.load(f)
    f.close()
    return data

def data_save(path,data):
    f = open(path,'w')
    json.dump(data,f,indent=True)
    f.close()

def customer_input(custlist):
    customer = {}
    customer['name'] = input('이름 -->')
    while True:
        customer['gender'] = input('성별(M,F) -->').upper()
        if customer['gender'] in ('M','F'):
            break
    while True:
        p = re.compile('[a-z][a-z0-9]{4,}@[a-z]{2,}[.](kr|com|org|net)$')
        while True:
            customer['email'] = input('email --> ')
            result = p.match(customer['email'])
            if result:
                break
            else:
                print('@를 포함하여 정확한 이메일을 기입하세요')
        check = 0
        for i in custlist:
            if customer['email'] == i['email']:
                check = 1
        if check == 0:
            break
        else:
            print('중복되는 이메일 있습니다. 다시 입력하세요')
    while True:
        customer['birth'] = input('출생년도 4자리 -->')
        if len(customer['birth']) == 4 and customer['birth'].isdigit:
            break
            
    custlist.append(customer)
    page = len(custlist)-1
    print(customer)
    print(custlist)
    return page 

def cur_page(custlist,page):
    if page < 0 :
        print('입력된 정보가 없습니다.')
    else:
        print(f'현재 페이지는 {page+1}페이지 입니다.')
        print(custlist[page])
    print(custlist) #점검용

def pre_page(custlist,page):
    if page <= 0:
        print(f'첫번째 페이지 입니다. 이전 페이지 이동 불가')
    else:
        page -= 1
        print(f'현재 페이지는 {page+1}페이지 입니다.')
    print(custlist[page])
    print(page)
    return page 

def nxt_page(custlist,page):
    if page <= 0:
        print(f'마지막 페이지 입니다. 다음 페이지 이동 불가')
    else:
        page -= 1
        print(f'현재 페이지는 {page+1}페이지 입니다.')
    print(custlist[page])
    print(page) 
    return page 
def customer_delete(custlist):
    print(custlist)
    email = input('삭제하려는 email >>> ')
    delok = 0
    for i in range(len(custlist)):
        if email == custlist[i]['email']:
            print('{} 고객님의 정보가 삭제됩니다.',format(custlist[i]['name']))
            del custlist[i]
            delok = 1
            break
        #return 안해도된다
    if delok == 0:
        print('등록되지 않은 고객입니다.')
    print(custlist)

def customer_update(custlist):
    while True:
        email = input('수정할 고객 이메일 -->')
        idx = -1
        for i in range(len(custlist)):
            if email == custlist[i]['email']:
                idx = i
                break
        if idx == -1:
            print('등록되지 않은 이메일입니다')
            break

        choice1 = input('''다음중 수정할 항목을 선택하세요(name,gender,birth)''')
        custlist[idx][choice1] = input('수정할 {}을 입력하세요 >>>'.format(choice1))
        print(custlist)
        break
        #return 안해도된다