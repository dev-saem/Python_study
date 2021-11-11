# 태극 모양 그리기

import turtle as t

t.bgcolor("black")
t.speed(0)

for x in range(200):
    if x % 3 == 0:    # 번갈아가면서 선 색 변경
        t.color("red")
    if x % 3 == 1:
        t.color("yellow")
    if x % 3 == 2:
        t.color("blue")
    t.forward(x*2)  # x*2만큼 앞으로 이동(반복하면서 선이 점점 길어짐)
    t.left(119)