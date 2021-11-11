# 키보드로 거북이 조종하여 그림 그리기

import turtle as t

def turn_right():   # 오른쪽 이동 함수
    t.setheading(0) # t.seth(0)과 동일
    t.forward(10)   # t.fd(10)과 동일

def turn_up():  # 위로 이동 함수
    t.setheading(90)
    t.forward(10)

def turn_left():    # 왼쪽 이동 함수
    t.setheading(180)
    t.forward(10)

def turn_down():    # 아래로 이동 함수
    t.setheading(270)
    t.forward(10)

def blank():    # 화면을 지우는 함수
    t.clear()

t.shape("turtle")
t.speed(0)
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(blank, "Escape")   # ESC를 누르면 blank 함수 실행
t.listen()  # 거북이 그래픽 창이 키보드 입력을 받음
t.mainloop()    # 사용자가 거북이 그래픽 창을 종료할 때까지 프로그램 실행