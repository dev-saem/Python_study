# 마음대로 걷는 거북이

import turtle as t
import random

t.shape("turtle")
t.speed(0)

# 1번쩨
# for x in range(500):
#     a = random.randint(1, 360)  # 1~360 사이 값으로 각도 랜덤 지정
#     t.setheading(a) # 거북이 방향을 a 각도로 돌림
#     t.forward(10)

# 2번째
for x in range(500):
    a = random.randint(1, 360)
    t.setheading(a)
    b = random.randint(1,20)
    t.forward(b)