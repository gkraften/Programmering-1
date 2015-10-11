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

def insertion_sort(l):
    for i in range(1, len(l)):
        j = i
        while j > 0 and l[j] < l[j-1]:
            temp = l[j]
            l[j] = l[j-1]
            l[j-1] = temp
            j -= 1

n = 100000
nums = [i for i in range(1, 2*n)]
the_list = []
for i in range(n):
    num = random.choice(nums)
    nums.remove(num)
    the_list.append(num)
nums = None

print(the_list)
#insertion_sort(the_list)
the_list.sort()
print(the_list)