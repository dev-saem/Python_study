# 마우스로 거북이 조종하여 그림 그리기

import turtle as t

t.speed(0)
t.pensize(2)
t.hideturtle()  # 거북이 화면에서 숨기기
t.onscreenclick(t.goto) # 마우스 버튼을 누르면 t.goto 함수 호출
# 그 위치로 거북이가 움직이면서 선을 그림
t.mainloop()