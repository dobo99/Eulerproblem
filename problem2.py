# -*-coding:utf8

# 짝수이면서 4백만 이하인 피보나치 수열 항들의 합은?

def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-2) + fib(n-1)

x = []
n = 2

while fib(n) > 4000000:
    if fib(n) % 2 == 0:
        x.append(fib(n))
        fib(n) == fib(n+1)
    else:
        fib(n) == fib(n+1)

print x