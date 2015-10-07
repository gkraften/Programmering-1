import random


def selection_sort(l):
    for current_pos in range(len(l)):
        min_pos = current_pos
        for pos in range(current_pos + 1, len(l)):
            if l[pos] < l[min_pos]:
                min_pos = pos
        if min_pos != current_pos:
            temp = l[current_pos]
            l[current_pos] = l[min_pos]
            l[min_pos] = temp

n = 1000
nums = [i for i in range(1, 2*n)]
the_list = []
for i in range(n):
    num = random.choice(nums)
    nums.remove(num)
    the_list.append(num)

print(the_list)
selection_sort(the_list)
print(the_list)