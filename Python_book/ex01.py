import turtle as t

# 삼각형 그리기
d = 200
t.color("red")  # 색 변경
# t.forward(d)  # 앞으로 100만큼 이동
# t.left(120) # 왼쪽으로 120도 회전
# t.forward(d)
# t.left(120)
# t.forward(d)
# t.left(120)

for x in range(3):
    t.forward(d)
    t.left(120)

# 사각형 그리기
t.color("green")
t.pensize(3)    # 펜 굵기 변경
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
for x in range(4):
    t.forward(d)
    t.left(90)

# 원 그리기
t.color("blue")
t.pensize(5)
t.circle(d/2)    # 반지름 지정