# 讓使⽤者輸入⼀個數列 
# 將該數列的總和與平均計算完畢後顯⽰在畫⾯上 
# 請輸入整數數列(空⽩分隔): 1 2 3 4 5 
# 數列為: 1 2 3 4 5 
# 總和 = 15 
# 平均 = 3.0
numList = list(map(int, input('請輸入整數數列(空白分隔): ').split()))

# 方法二: 直接用sum(list)，計算列表裡數字的總和
print(f"數列為:", end = ' ')
for num in numList:
    print(f"{num}", end = ' ')
print(f"\n總和 = {sum(numList)}")
print(f"平均 = {sum(numList) / len(numList)}")

# 方法一: 直覺想法
sum = 0
print(f"數列為:", end = ' ')
for num in numList:
    print(f"{num}", end = ' ')
    sum += num
print(f"\n總和 = {sum}")
print(f"平均 = {sum / len(numList)}")
