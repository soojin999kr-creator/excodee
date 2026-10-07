import math

# 1. 수식 계산
a, b, c = 3, 4, 5
res1 = 1 / (1 + a/b + c)
print(f"1번 결과: {res1}")

# 2. 2차방정식 근 구하기
a_eq, b_eq, c_eq = 1, 1, -6
x1 = (-b_eq + math.sqrt(b_eq**2 - 4*a_eq*c_eq)) / (2*a_eq)
x2 = (-b_eq - math.sqrt(b_eq**2 - 4*a_eq*c_eq)) / (2*a_eq)
print(f"2번 두 근: {x1}, {x2}")

# 3. 원의 면적
r = 5
area = math.pi * (r ** 2)
print(f"3번 원의 면적: {area}")

# 4. beta
beta, g = 2.0, 3.2
res4 = beta * math.exp(-g)
print(f"4번 결과: {res4}")

# 5. 정규분포 관련 수식
x_val, mu, rho = 0, 1.5, 2.0
res5 = (1 / math.sqrt(2 * math.pi * rho)) * math.exp(((x_val - mu)**2) / (2 * (rho**2)))
print(f"5번 결과: {res5}")