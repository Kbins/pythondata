# 수자 맞추기 게임

# 컴퓨터가 두 수의 사칙연산 문제를 내면 맟추는 게임
# 이때 두 수는 랜덤으로 선택, 연산자도 랜덤으로 선택
# 나누기의 경우 소수 이하 값은 정수로 변경해서 처리
# 문제는 종료를 선택할때까지 반복
# 맞춘 문제수/총 문제수 종료 시 출력
# random.randint(start,end)
# random.choice()

import random
total = 0
hit = 0
oper = ['+','-','*','/']
while True:
    
    a = random.randint(1,50)
    b = random.randint(1,50)
    op = random.choice(oper)
    quiz = str(a) + op + str(b)
    print(quiz)
    result = int(input('>>> '))
    total += 1
    if result == int(eval(quiz)):
        print('정답')
        hit +=1
    print('오답')
    if 'Q' == input('종료(Q)'):
        break
print(f'맟춘 문항수:{hit}/전체 문항수{total}')