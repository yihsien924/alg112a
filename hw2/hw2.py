#法一
def power2n1(n):
    return 2**n
print(power2n1(5))

#法二
def power2n2(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    return power2n2(n-1) + power2n2(n-1)
print(power2n2(5))

#法三
def power2n3(n):
    if n == 0:
        return 1
    return 2*power2n3(n-1)
print(power2n3(5))

#法四
fib = [None]*10000
fib[0] = 0
fib[1] = 2

def power2n4(n):
    if n < 0: raise
    if not fib[n] is None: return fib[n]   #存在數字直接輸出，為none進下一行計算
    fib[n] = power2n4(n - 1) + power2n4(n- 1) #ex:2的三次方+2的三次方=2的四次方
    return fib[n]
print(power2n4(5))