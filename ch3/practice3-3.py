# 使⽤者輸入起與⽌的數字，可以顯⽰差為 1 的等差數列與其總和
# 起始值: 1  (不一定從1開始)
# 終⽌值：40 (不一定是10的倍數)
# 01 02 03 04 05 06 07 08 09 10  
# 11 12 13 14 15 16 17 18 19 20  
# 21 22 23 24 25 26 27 28 29 30  
# 31 32 33 34 35 36 37 38 39 40  
# 總和: 820
start = int(input('輸入起始值: '))
stop = int(input('輸入終止值: '))
sum = 0
count = 0 
for i in range(start, stop+1):
    if i < 10:
        print(f"0", end='')
    print(i, end=" ")
    count += 1
    if count % 10 == 0: # 每10個一排
        print()
    sum += i
print(f"\n總和: {sum}")