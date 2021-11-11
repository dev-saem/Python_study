# 계산 문제 맞히기

import random

def make_question():
    a = random.randint(1, 40)
    b = random.randint(1, 20)
    op = random.randint(1, 3)

    # 문자열 변수 q에 문제 만듬
    q = str(a)

    # 연산자 추가
    if op == 1: # op값이 1이면 덧셈 문제
        q = q + "+"
    if op == 2: # op값이 2이면 뺄셈 문제
        q = q + "-"
    if op == 3: # op값이 3이면 곱셈 문제
        q = q + "*"

    q = q + str(b)
    return q

# 정답, 오답 변수 초기화
sc1 = 0
sc2 = 0

for x in range(5):  # 다섯 문제 풀기
    q = make_question() # 문제 만들기
    print(q)    # 문제 출력
    ans = input("=")    # 정답 입력 받기
    r = int(ans)    # 정답을 정수로 변환

    # 컴퓨터가 계산한 결과 eval(q)값과 사용자 결과값(r) 비교
    if eval(q) == r:
        print("정답!")
        sc1 += 1
    else:
        print("오답!")
        sc2 += 1

print("정답 : ", sc1, "오답 : ", sc2)
if sc2 == 0:    # 오답이 0개일 때
    print("당신은 천재입니다!")