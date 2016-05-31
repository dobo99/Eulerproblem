# -*-coding:utf8

# 짝수이면서 4백만 이하인 피보나치 수열 항들의 합은?

x = [1, 2] # 피보나치 수열의 시작점

while x[-1] <= 4000000:
    number = x[-2] + x[-1]
    x.append(number)
# 4백만 이하의 피보나치 수열을 구한다. append는 리스트의 오른쪽에 들어간다.

y = []
for num in x:
    if num % 2 == 0:
        y.append(num)
    else:
        del num
# x는 4백만 이하의 피보나치 수열이다. 그 중 짝수를 y에 넣는다

print y
print sum(y)
# 짝수인 수열과 그 총합