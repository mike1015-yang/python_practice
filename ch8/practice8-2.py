# 定義正立⽅體 (Cube) 類別，內有邊長屬性(length) 
# 並⽤ private 封裝，有建構式與 setter、getter 
# 呼叫建構式或 setter 設定邊長時，如果傳入的值為 0 或負數，
# 會拋出⾃定的 CubeError，並顯⽰「正立⽅體邊長不可為0或負數」 
# 使⽤者輸入的邊長必須為數字，如果為錯誤格式，顯⽰「數字格式不正確！」 
# 輸入的邊長如果正確，會顯⽰體積
# ----------------------------------------------------------
# 立⽅體邊長: 0 
# CubeError: 正立⽅體邊長不可為0或負數，請重新輸入 
# 立⽅體邊長: a 
# 數字格式不正確，請重新輸入 
# 立⽅體邊長: 3 
# 邊長: 3.0, 體積: 27.0

import math
class CubeError(BaseException):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"CubeError: {self.message}"
    
class Cube:
    def __init__(self, length):
        self.__length = 0.0
        self.not_length = length
    
    @property
    def get_length(self):
        return self.__length
    
    @get_length.setter
    def not_length(self, length):
        if length.isalpha():
            raise CubeError(f"數字格式不正確，請重新輸入")
        elif float(length) <= 0:
            raise CubeError(f"正立⽅體邊長不可為0或負數，請重新輸入")
        else:
            self.__length = length
            
    def __str__(self):
        return f"邊長: {float(self.__length)}, 體積: {math.pow(float(self.__length), 3)}"     
while True:    
    try:
        num = input(f"立⽅體邊長: ")
        cube = Cube(num)
        print(cube)
        break
    except CubeError as err:
        print(err)

