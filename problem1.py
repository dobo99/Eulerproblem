# -*-coding:utf8

# 1000보다 작은 자연수 중 3 또는 5의 배수를 모두 더하면?

x = range(1, 1000)
y = []

for number in x:
    if number % 3 == 0 or number % 5 == 0:
        y.append(number)

print sum(y)