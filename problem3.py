# -*-coding:utf8

# 600851475143의 소인수 중 가장 큰 수

x = range(1,1000)
y = []

for number in x:
    if 600851475143 % number == 0:
       y.append(number)
    else:
        del number

print y
print 600851475143 / y.pop(1)