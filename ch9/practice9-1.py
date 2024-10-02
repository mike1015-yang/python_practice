# 使⽤者可以輸入多列資料 
# 沒有輸入資料直接按 Enter 鍵會結束輸入 
# 結束後會⾃動將輸入內容存檔
# -------------------------------------
# 輸入資料 (或直接按 Enter 結束):  
# 1. ⽔果 
# 2. 鮮奶 
# 3. 麵包
#  
# 存檔完畢!

import os

def write(file):
    
    text = input(f"輸入資料(或直接按Enter結束):\n")
    if text == '':
        print(f"存檔完畢!")
    else:
        with open(file, 'w', encoding='UTF-8') as f:
                f.write(f"{text}\n")
        while True:
            text = input()
            with open(file, 'a', encoding='UTF-8') as f:
                f.write(f"{text}\n")
            if text == '':
                print(f"存檔完畢!")
                break
writeDir = 'practice9-1'
if not os.path.isdir(writeDir):
    os.makedirs(writeDir)
write(f"{writeDir}/list.txt")