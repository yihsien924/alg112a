import numpy as np

def gradient_descent(f, initial_solution, learning_rate=0.01, max_iterations=1000, epsilon=1e-6, step=1e-6):
    current_solution = np.array(initial_solution)
    
    for iteration in range(max_iterations):
        gradient = grad(f, current_solution, step)
        current_solution -= learning_rate * gradient

        current_value = f(current_solution)
        print(f"Iteration {iteration + 1}: Current Solution = {current_solution}, Value = {current_value}")

        if np.linalg.norm(gradient) < epsilon:
            break  #如果梯度的範數足夠小，停止優化

    return current_solution, f(current_solution)

def df(f, p, k, step):
    p1 = p.copy()
    p1[k] = p[k] + step
    return (f(p1) - f(p)) / step

def grad(f, p, step=1e-6):
    gp = p.copy()
    for k in range(len(p)):
        gp[k] = df(f, p, k, step)
    return np.array(gp)

#測試
def f(x):
    return x[0]**2 + x[1]**2 + x[2]**2

initial_solution = [2, 1, 3]  #初始解
final_solution, final_value = gradient_descent(f, initial_solution)

print( final_solution,final_value)