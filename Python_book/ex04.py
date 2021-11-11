import turtle as t

# 선 반복 그리기
angle = 90  # 거북이가 왼쪽으로 회전할 각도 지정
t.bgcolor("black")
t.color("yellow")
t.speed(0)
for x in range(200):
    t.forward(x)    # 실행 반복하면서 선이 길어짐
    t.left(angle)