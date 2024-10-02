# ⼤樂透號碼總共有 6 個號碼加 1 個特別號，⽽且都不重複 
# 利⽤亂數產⽣⼀組⼤樂透號碼，除了特別號以外，其他 6 個號碼由⼩到⼤排序 
# ⼤樂透號碼都是1~49，可使⽤ random.randint(1, 49) 產⽣
# 開獎，⼤樂透號碼為:  
# 38 11 43 13 15 23 特別號: 29 
# 由⼩到⼤排列: 
# 11 13 15 23 38 43 特別號: 29

import random

sev_set = set()
while len(sev_set) < 7:
    sev_set.add(random.randint(1, 49))

num_list = list(sev_set)
special_num = num_list[-1]
num_list.pop()
print(f"開獎，大樂透號碼為:")
for num in num_list:
    print(f"{num}", end = " ")
print(f"特別號: {special_num}\n由小到大排列:")

# 排序方法一: 用官方函式(.sort())
num_list.sort()
for num in num_list:
    print(f"{num}", end = " ")
print(f"特別號: {special_num}")

# 排序方法二: BubbleSort
for i in range(len(num_list) - 1):
    change = False
    for j in range(len(num_list) - i -1):
        if num_list[j] > num_list[j+1]:
            temp = num_list[j+1]
            num_list[j+1] = num_list[j]
            num_list[j] = temp
            change = True
        else:
            continue
    if not change:
        break

for num in num_list:
    print(f"{num}", end = " ")
print(f"特別號: {special_num}")
