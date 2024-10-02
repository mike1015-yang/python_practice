# 輸入要產⽣幾個 1～100 (不含) 整數後按確定，會使⽤亂數產⽣對應個數的整數，
# 並檢查是否為質數
#---------------------------------------------------------------------
# 使⽤亂數產⽣幾個 1～100 (不含) 整數？ 5 
# 18 不是質數 
# 60 不是質數 
# 21 不是質數 
# 83 是質數 
# 14 不是質數
import random
import math
num = int(input(f"使用亂數產生幾個1~100(不含)整數? "))
for i in range(num):
    n = random.randrange(1, 100)
    if_prnum = True
    for i in range(2,math.ceil(math.sqrt(n))):
        if n % i == 0:
            print(f"{n}不是質數")
            if_prnum = False
            break
        else:
            continue
    if if_prnum:
        print(f"{n}是質數")