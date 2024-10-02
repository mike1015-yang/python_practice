# 定義1個 calculate(numbers)，共有 2 個回傳值 
# 計算numbers所有元素的總和與平均值並回傳 (回傳總和與平均) 
# 讓使⽤者輸入⼀個數列，輸入完畢後呼叫上述 calculate 函式運算，
# 並將回傳的總和與平均顯⽰在畫⾯上 
# 請輸入整數數列(空⽩分隔): 1 2 3 4 5 
# 數列為: 1 2 3 4 5 
# 總和 = 15 
# 平均 = 3.0

def calculate(numbers):
    sum = 0
    print(f"數列為:", end = " ")
    for num in numbers:
        print(f"{num}", end = " ")
        sum += num
    avg = sum / len(numbers)
    return sum, avg
    
num_list = list(map(int, input("請輸入整數數列(空白分隔): ").split()))
result = calculate(num_list)
print(f"\n總和 = {result[0]}\n平均 = {result[1]}")