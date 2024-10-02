# ⼩華⼗分熱衷⼤樂透，但他不選不吉利數字，如果他輸入 4（可以輸入1~9數字，輸入錯誤要求重新輸入），
# 代表 1~49 個可選擇的⼤樂透數字中，無論個位數或⼗位數有 4 的數字（例如：4、14、45），
# 他都不選，程式要能顯⽰剩下他可以選擇的數字有哪些？並且將這些數字的總個數也⼀併顯⽰出來
# 不吉利數字 (1 ~ 9) : 12 
# 輸入錯誤，請再輸入⼀次 
# 不吉利數字 (1 ~ 9) : 4 
# 01 02 03 05 06 07 08 09 10 11  
# 12 13 15 16 17 18 19 20 21 22  
# 23 25 26 27 28 29 30 31 32 33  
# 35 36 37 38 39  
# 總個數: 35
while 1:
    noNumber = int(input('不吉利數字(1~9): '))
    if noNumber > 9 or noNumber < 1:
        print('輸入錯誤，請再輸入一次')
        continue
    else:
        break
count = 0
for i in range(1, 50):
    if i // 10 == noNumber or i % 10 == noNumber: # x // y 會顯示商
        continue
    else:
        if i < 10:
            print(f"0", end='')
        print(i, end=' ')
        count += 1
        if count % 10 == 0:
            print()
print(f"\n總個數: {count}")
        