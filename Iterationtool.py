from itertools import product

k_m = list(map(int, input().split()))

K = k_m[0]
M = k_m[1]

list_of_elements = []

for i in range(K):
    ls = list(map(int, input().split()))
    ls.remove(ls[0])
    list_of_elements.append(ls)


possible_combination = list(product(*list_of_elements))


def func(nums):
    return sum(x*x for x in nums) % M

lp = list(map(func, possible_combination))

print(max(lp))