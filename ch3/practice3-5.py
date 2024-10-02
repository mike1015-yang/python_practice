# 九九乘法表
# 巢狀迴圈
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} X {j} = {i*j:2}", end='  ') # :2，對齊右邊兩個字元
    print()