#使用ChatGPT輔助理解
import numpy as np

def solve_polynomial(coefficients):
    #將係數轉換為 NumPy 陣列
    coefficients = np.array(coefficients)

    #求解多項式的根
    roots = np.roots(coefficients)

    return roots

if __name__ == "__main__":

    input_coefficients = input("請輸入多項式的係數，以空格分隔：")
    
    #將使用者輸入的係數轉換為浮點數列表
    coefficients = [float(coef) for coef in input_coefficients.split()]

    #求解多項式的根
    roots = solve_polynomial(coefficients)

    print(f"多項式的根為：{roots}")