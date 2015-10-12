import random
import time
from multiprocessing import Process, Queue


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
selection_sort.name = "Selection sort"

def insertion_sort(l):
    for i in range(1, len(l)):
        j = i
        while j > 0 and l[j] < l[j-1]:
            temp = l[j]
            l[j] = l[j-1]
            l[j-1] = temp
            j -= 1
insertion_sort.name = "Insertion sort"

results = []
def run_test(algorithm, l, q):
    global results
    tm = time.clock()
    algorithm(l)
    duration = time.clock() - tm
    q.put(algorithm.name + ": {}s".format(duration))

n = 10000
nums = [i for i in range(1, 2*n)]
the_list = []
for i in range(n):
    num = random.choice(nums)
    nums.remove(num)
    the_list.append(num)
nums = None

list2 = the_list[:]
list3 = the_list[:]

q = Queue()
print("Running tests")
threads = (Process(target=run_test, args=(selection_sort, the_list, q)), Process(target=run_test, args=(selection_sort, the_list, q)), Process(target=run_test, args=(insertion_sort, list2, q)), Process(target=run_test, args=(insertion_sort, list2, q)))
for t in threads:
    t.start()
for t in threads:
    t.join()

while not q.empty():
    print(q.get())