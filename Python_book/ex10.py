# 1부터 n까지 합 구하기

def sum_func(n):
    s = 0
    for x in range(1, n+1):
        s = s + x
    return s

print(sum_func(10))
print(sum_func(100))

# 1부터 n까지 곱 구하기
def factorial(n):
    fact = 1
    for x in range(1, n+1):
        fact = fact * x
    return fact

print(factorial(5))
print(factorial(10))