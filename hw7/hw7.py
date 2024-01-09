import numpy as np
from micrograd import Tensor

def gradient_descent(f, initial_solution, learning_rate=0.01, max_iterations=1000, epsilon=1e-6):
    current_solution = np.array(initial_solution, dtype=np.float32)
    current_solution = [Tensor(x) for x in current_solution]

    for iteration in range(max_iterations):
        gradient = grad(f, current_solution)
        current_solution = [p - learning_rate * g for p, g in zip(current_solution, gradient)]

        current_value = f(*current_solution).data
        print(f"Iteration {iteration + 1}: Current Solution = {[p.data for p in current_solution]}, Value = {current_value}")

        if np.linalg.norm([g.data for g in gradient]) < epsilon:
            break  #如果梯度的範數足夠小，停止優化

    return [p.data for p in current_solution], current_value

def grad(f, p):
    result = []
    for i in range(len(p)):
        p[i].zero_grad()
        loss = f(*p)
        loss.backward()
        result.append(p[i].grad)
    return result

#測試
def f(x, y, z):
    return x**2 + y**2 + z**2

initial_solution = [2.0, 1.0, 3.0]  #初始解
final_solution, final_value = gradient_descent(f, initial_solution)

print("最終解：", final_solution, "最終值：", final_value)