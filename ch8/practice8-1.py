# 被除數與除數皆正確，顯⽰運算結果 
# 被除數或除數格式錯誤，例如輸入a
# 顯⽰「被除數或除數格式錯誤」 
# 除數輸入 0，顯⽰「除數不可為0，請再重新輸入」
#-----------------------------------------
# 輸入被除數(整數): a 
# 被除數或除數格式錯誤，請重新輸入 
# 輸入被除數(整數): 10 
# 輸入除數(整數): 0 
# 除數不可為0，請重新輸入 
# 輸入被除數(整數): 10 
# 輸入除數(整數): 3 
# 10 ÷ 3 = 3 ... 1

while True:
    try:
        dividend = int(input(f"輸入被除數(整數): "))
        divisor = int(input(f"輸入除數(整數): "))
        ans = dividend // divisor
        mod = dividend % divisor
    except ValueError:
        print(f"被除數或除數格式錯誤，請重新輸入")
    except ZeroDivisionError:
        print(f"除數不可為0，請重新輸入")
    else:
        print(f"{dividend} / {divisor} = {ans} ... {mod}")
        break