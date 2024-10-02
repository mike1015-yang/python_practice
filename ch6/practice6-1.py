# 建立 1 個長⽅體 (Cuboid) 類別，內容包含 
# 屬性：長 (length)、寬 (width)、⾼ (height) 
# ⽅法  
# volume() ⽅法：計算完體積並回傳 
# getInfo() ⽅法：回傳長、寬、⾼與體積 
# 建構式：設定屬性初始值 
# 主流程 
# 將使⽤者輸入的長、寬、⾼建立 Cuboid 物件，並顯⽰該物件長、寬、⾼與體積
# 請輸入長⽅體的長、寬、⾼(空⽩間隔): 1 2 3 
# 輸入的長⽅體資訊如下:  
# 長: 1.0, 寬: 2.0, ⾼: 3.0, 體積: 6.0

# class Cuboid:
#     def __init__(self, length=0, width=0, height=0, body=0):
#         self.length = length
#         self.width = width
#         self.height = height
#         self.body = body
#     def volume(self):
#         self.body = self.length * self.width * self.height
#         return self.body
#     def getInfo(self):
#         print(f"長: {self.length}", end = ", ")
#         print(f"寬: {self.width}", end = ", ")
#         print(f"高: {self.height}", end = ", ")
#         print(f"體積: {self.body}")
# num_list = list(map(float,(input(f"請輸入長方體的長、寬、高(空白間隔): ").split())))
# print(f"輸入的長方體資訊如下:")
# cuboid1 = Cuboid(num_list[0], num_list[1], num_list[2])
# cuboid1.volume()
# cuboid1.getInfo()

class Cuboid:
    def __init__(self, length=0, width=0, height=0):
        self.length = length
        self.width = width
        self.height = height
    def volume(self):
        return self.length * self.width * self.height
    def getInfo(self):
        print(f"長: {self.length}", end = ", ")
        print(f"寬: {self.width}", end = ", ")
        print(f"高: {self.height}", end = ", ")
# 以下可以設多個變數來接list
length, width, height = list(map(float,(input(f"請輸入長方體的長、寬、高(空白間隔): ").split())))
print(f"輸入的長方體資訊如下:")
cuboid1 = Cuboid(length, width, height)
cuboid1.getInfo()
print(f"體積: {cuboid1.volume()}")

