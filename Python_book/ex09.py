# 함수 정의 및 호출
def hello():
    print("Hello Python")

hello()
hello()
hello()

# 인자가 있는 함수
def hello2(name):
    print("Hello", name)

hello2("John")
hello2("Mike")

# 결과값이 있는 함수
def square(a):  # a의 제곱을 구하는 함수
    c = a * a
    return c

def triangle(a, h): # 밑변 a, 높이 h인 삼각형 넓이
    c = a * h / 2
    return c

s1 = 4
s2 = square(s1)
print(s1, s2)
print(triangle(3, 4))