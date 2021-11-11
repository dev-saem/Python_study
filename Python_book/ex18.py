# 터틀런 만들기

import turtle as t
import random

score = 0   # 점수 저장 변수
playing = False # 현재 게임이 플레이 중인지 확인하는 변수

te = t.Turtle() # 악당 거북이 te, 빨간색
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0, 200)

ts = t.Turtle() # 먹이 ts, 초록색 동그라미
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up()
ts.goto(0, -200)

# 방향 변경 함수
def turn_right():
    t.setheading(0)

def turn_up():
    t.setheading(90)

def turn_left():
    t.setheading(180)

def turn_down():
    t.setheading(270)

# 게임 시작 함수
def start():
    global playing
    if playing == False:
        playing = True
        t.clear()   # 메세지 지우기
        play()

# 게임을 실제로 플레이하는 함수
def play():
    global score
    global playing
    t.forward(10)   # 주인공 거북이가 10만큼 앞으로 이동
    if random.randint(1, 5) == 3:   # 1~5 사이에서 뽑은 수가 3이면(20% 확률)
        ang = te.towards(t.pos())
        te.setheading(ang)  # 악당 거북이가 주인공 거북이를 바라봄
    speed = score + 5   # 점수에 5를 더해서 속도를 올림, 점수가 올라가면 빨라짐
    
    if speed > 15:  # 속도가 15를 넘기지 않도록 설정
        speed = 15
    te.forward(speed)
    
    if t.distance(te) < 12: # 주인공과 악당의 거리가 12보다 작으면 게임 종료
        text = "Score : " + str(score)
        message("Game Over", text)
        playing = False
        score = 0

    if t.distance(ts) < 12: # 주인공과 먹이의 거리가 12보다 작으면(가까우면)
        score += 1  # 점수 증가
        t.write(score)  # 점수 화면 표시
        star_x = random.randint(-230, 230)
        star_y = random.randint(-230, 230)
        ts.goto(star_x, star_y) # 먹이를 다른 곳으로 이동
    if playing:
        t.ontimer(play, 100)    # 게임 플레이 중이면 0.1초 후 play 함수 실행

# 메세지 화면 출력 함수
def message(m1, m2):
    t.clear()
    t.goto(0, 100)
    t.write(m1, False, "center", ("", 20))
    t.goto(0, -100)
    t.write(m2, False, "center", ("", 15))
    t.home()

t.title("Turtle Run")
t.setup(500, 500)
t.bgcolor("orange")
t.shape("turtle")   # 거북이 모양 커서 사용
t.speed(0)
t.up()
t.color("white")
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(start, "space")
t.listen()  # 거북이 그래픽 창이 키보드 입력을 받도록 설정
message("Turtle Run", "[Space]")
play()  # 게임 시작
t.mainloop()
