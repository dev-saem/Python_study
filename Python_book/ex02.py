import turtle as t

# 정오각형 그리기
n = 5 
t.color("purple")
t.begin_fill()  # 색칠할 영역 시작
for x in range(n):
    t.forward(50)
    t.lt(360/n)
t.end_fill()    # 색칠할 영역 끝