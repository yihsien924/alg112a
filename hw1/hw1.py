def fib(n): #fib = Fₙ = Fₙ-₁ + Fₙ-₂
    if n <= 1:
        return n
    
    fib = [0] * (n + 1) #初始化一個列表fib，用來存儲費氏數列的數字(創建了包含0的(n+1)個列表)
    fib[1] = 1 #第二的數字為1
    
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n] #返回 fib[n] 的值

n = 6  #測試
result = fib(n)
print(result)