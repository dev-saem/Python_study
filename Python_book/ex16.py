# 타자 게임

import random
import time

# 단어 리스트
w = ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf"]
n = 1   # 문제 번호
print("[타자 게임] 준비되면 엔터!")
input() # 사용자가 엔터를 누를때까지 기다림
start = time.time() # 시작 시간 기록

q = random.choice(w)    # 단어 리스트에서 아무것이나 하나 뽑음
while n <= 5:
    print("문제", n)
    print(q)    # 문제 보여줌
    x = input() # 사용자 입력 받음
    if q == x:  # 문제와 입력이 같을 때
        print("통과!")
        n = n+1 # 문제 번호 1 증가
        q = random.choice(w)    # 새 문제를 뽑음
    else:
        print("오타! 다시 도전!")

end = time.time()   # 끝난 시간 기록
et = end - start  # 실제로 걸린 시간 계산
et = format(et, ".2f")  # 소수점 둘째 자리까지 표시
print("타자 시간 : ", et, "초")