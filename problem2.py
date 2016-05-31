# -*-coding:utf8

# 짝수이면서 4백만 이하인 피보나치 수열 항들의 합은?

x = [1, 2]

while x[-1] <= 4000000:
    number = x[-2] + x[-1]
    x.append(number)

y = []
for num in x:
    if num % 2 == 0:
        y.append(num)
    else:
        del num

print y
print sum(y)
