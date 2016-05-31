# -*-coding:utf8

# 600851475143의 소인수 중 가장 큰 수

x = range(1,1000) # 소인수 중 가장 작은수를 구하기 위한 임의의 구간
y = [] # 빈 리스트

for number in x:
    if 600851475143 % number == 0:
       y.append(number)
    else:
        del number
# x속 수들 중 600851475143의 소인수를 찾는다.

print y # 구한 소인수를 본다
print 600851475143 / y.pop(1) # 최소의 소인수로 600851475143을 나누면 최대 소인수를 구할 수 있다.