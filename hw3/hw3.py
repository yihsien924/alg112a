from itertools import permutations

def generate_permutations(input_list):
    all_permutations = list(permutations(input_list))
    return all_permutations

# 測試程式碼
user_input = input("輸入（以空格分隔元素）：")
input_list = user_input.split()
all_permutations = generate_permutations(input_list)

for perm in all_permutations:
    print(perm)