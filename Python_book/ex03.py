import turtle as t

# 원 반복 그리기
n = 50  # 원 갯수
t.bgcolor("black")  # 배경색 지정
t.color("green")    # 펜 색 지정
t.speed(0)  # 거북이 속도 지정
for x in range(n):
    t.circle(80)    # 원 반지름
    t.left(360/n)   # 왼쪽으로 회전