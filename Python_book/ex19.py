# 집합 연산 프로그램

# 파이썬의 집합 기능 1
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A)
print(B)

print(1 in A)
print(6 in A)
print(len(A))

print(A|B)  # 합집합
print(A&B)  # 교집합
print(A-B)  # 차집합

# 파이썬의 집합 기능 2
C = {x for x in range(1, 11)}
D = {x for x in range(1, 11) if x % 3 == 0}

print(C)
print(D)

print(C<D)  # C는 D의 부분집합?
print(C>D)  # D는 C의 부분집합?