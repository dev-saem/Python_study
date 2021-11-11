# 1부터 10까지 숫자 합계 구하기

print("for 문 사용")
s = 0
for x in range(1, 10+1):
    s = s+x
    print("x : ", x, ", sum : ", s)

print()

print("while 문 사용")
s = 0
x = 1
while x <= 10:
    s = s + x
    print("x : ", x, ", sum : ", s)
    x = x + 1