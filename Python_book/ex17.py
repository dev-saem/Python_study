# 거북이 대포 게임 만들기

import turtle as t
import random

def turn_up():
    t.left(2)

def turn_down():
    t.right(2)

def fire(): # spaceBar 누르면 거북이 대포 발사
    ang = t.heading()   # 현재 거북이가 바라보는 각도 기억
    while t.ycor() > 0: # 거북이가 땅 위에 있는 동안 반복
        t.forward(15)
        t.right(5)

    # while 반복문을 빠져나오면 거북이가 땅에 닿은 상태
    d = t.distance(target, 0)   # 거북이와 목표 지점과의 거리
    t.sety(random.randint(10, 100)) # 성공, 실패 표시 위치 지정
    if d < 25:  # 거리 차이가 25보다 작으면 목표 지점에 명중한 것으로 처리
        t.color("blue")
        t.write("Good!", False, "center", ("", 15))
    else:
        t.color("red")
        t.write("Bad!", False, "center", ("", 15))
        t.color("black")    # 거북이 색을 검은색으로 되돌림
        t.goto(-200, 10)    # 거북이 위치를 처음 발사했던 곳으로 되돌림
        t.setheading(ang)   # 각도도 처음 기억해 둔 각도로 되돌림

# 땅을 그림
t.goto(-300, 0)
t.down()
t.goto(300, 0)

# 목표 지점 설정하고 그리기
target = random.randint(50, 150)
t.pensize(3)
t.color("green")
t.up()
t.goto(target - 25, 2)
t.down()
t.goto(target + 25, 2)

# 거북이 색을 검은색으로 지정하고 처음 발사했던 곳으로 되돌림
t.color("black")
t.up()
t.goto(-200, 10)
t.setheading(20)

# 거북이가 동작하는 데 필요한 설정
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(fire, "space")
t.listen()
t.mainloop()