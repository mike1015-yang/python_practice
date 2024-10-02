# 使⽤者輸入春、夏、秋、冬任⼀季節，會顯⽰該季節對應描述 
# 春：春暖花開 
# 夏：夏⽇炎炎 
# 秋：秋⾼氣爽 
# 冬：冬風凜冽
season = input('請輸入你喜愛的季節: ')
method = input("選擇方法，1.match，2.if-else: ")
match method:
    case '1':
        match season.lower():
            case '春' | 'spring':
                print(f"{season}:春暖花開")
            case '夏' | 'summer':
                print(f"{season}:夏日炎炎")
            case '秋' | 'autumn':
                print(f"{season}:秋高氣爽")
            case '冬' | 'winter':
                print(f"{season}:冬風凜冽")
            case _:
                print('輸入錯誤')
        print('使用match')
    # case '2':
    #     if season == '春' or season =='spring':
    #         print(f"{season}:春暖花開")
    #     elif season == '夏' or season == 'summer':
    #         print(f"{season}:夏日炎炎")
    #     elif season == '秋' or season == 'autumn':
    #         print(f"{season}:秋高氣爽")
    #     elif season == '冬' or season == 'winter':
    #         print(f"{season}:冬風凜冽")
    #     else:
    #         print('輸入錯誤')
    #     print('使用if-else')

