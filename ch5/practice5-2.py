# 定義 1 個函式: calculate(numbers, myFunction) 
# numbers: ⼀個數列 
# myFunction: ⼀個函式會計算 numbers 所有元素的平均值後顯⽰在畫⾯上 
# 讓使⽤者輸入⼀個數列，會將平均顯⽰在畫⾯上 
# 請輸入整數數列(空⽩分隔): 1 2 3 4 5 
# 數列為: 1 2 3 4 5 
# 平均 = 3.0

def calculate(numbers, myFunction):
    print(f"數列為:", end = " ")
    for num in numbers:
        print(f"{num}", end = " ")
    avg = myFunction(numbers)
    print(f"\n平均 = {avg}")

def avg(numbers):
    sum = 0
    for num in numbers:
        sum += num
    avg = sum / len(numbers)
    return avg

num_list = list(map(int, input(f"請輸入整數數列(空白分隔): ").split()))
calculate(num_list, avg)