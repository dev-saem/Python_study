# 숫자 추측하여 맞히기

import random

n = random.randint(1, 30)

while True: # 영원히 반복
    x = input("맞혀 보세요? ")
    g = int(x)  # 입력 받은 값 정수 변환
    if g == n:
        print("정답")
        break   # 정답을 맞히면 while 반복 블록 탈출
    if g < n:
        print("너무 작아요.")
    if g > n:
        print("너무 커요.")