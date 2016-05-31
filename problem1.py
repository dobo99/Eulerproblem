# -*-coding:utf8

# 1000보다 작은 자연수 중 3 또는 5의 배수를 모두 더하면?

x = range(1, 1000) # 1000보다 작은 자연수 리스트
y = [] # 계산을 위한 빈 리스트

for number in x:
    if number % 3 == 0 or number % 5 == 0:
        y.append(number)
# x 리스트에 있는 수들 중 3의 배수나 5의 배수를 y리스트로 넣는다.

print sum(y) # y속 수들의 총합