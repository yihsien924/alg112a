#使用ChatGPT輔助解釋
import random

def hillClimbing(f, initial_solution, h=0.01):
    fail_count = 0 
    while fail_count < 10000:  #如果失敗次數小於一萬次就繼續執行
        f_now = f(*initial_solution)  #f_now 為目前高度
        new_solution, f_new = neighbor(f, initial_solution, h)
        if f_new >= f_now:  #如果移動後高度比現在高
            f_now = f_new  #就移過去
            initial_solution = new_solution
            print('Solution:', initial_solution, 'Value:', f_now)
            fail_count = 0  
        else: 
            fail_count += 1  #又失敗一次
    return initial_solution, f_now  #結束傳回（已經失敗超過一萬次了）

def neighbor(f, solution, h=0.01):
    new_solution = [s + random.uniform(-h, h) for s in solution]  #產生新解
    return new_solution, f(*new_solution)

#測試
def f(x, y, z):
    return -1 * (x**2 + y**2 + z**2)

initial_solution = [2, 1, 3]  #初始解
final_solution, final_value = hillClimbing(f, initial_solution)

print( final_solution, final_value)