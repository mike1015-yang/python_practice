# 讓使⽤者輸入被除數與除數，整數除法後取其商與餘數
dividend = int(input("請輸入被除數: "))
divisor = int(input('請輸入除數: '))
print(f"{dividend} // {divisor} = {dividend // divisor}...{dividend % divisor}")

