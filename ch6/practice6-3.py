# 承襲 6-2，但再建立 1 個長⽅體類別的⼦類別：房屋 (House) 類別，內容包含 
# 屬性：增加材質 (material) 屬性 
# ⽅法：覆寫getInfo()⽅法：除了回傳長、寬、⾼與體積外，還能回傳材質 
# 建構式：設定長、寬、⾼、材質等 4 屬性的初始值 
# 主流程 
# 詢問使⽤者欲輸入的房屋總個數 
# 讓使⽤者輸入指定個數的房屋資訊，並顯⽰所有輸入房屋的長、寬、⾼與體積
# 請問有幾間房屋? 3 
# 請輸入第1間房屋的長、寬、⾼與材質(空⽩間隔): 1 1 1 C 
# 請輸入第2間房屋的長、寬、⾼與材質(空⽩間隔): 2 2 2 B 
# 請輸入第3間房屋的長、寬、⾼與材質(空⽩間隔): 3 3 3 A 
# 輸入的3間房屋資訊如下: 
# 長: 1.0, 寬: 1.0, ⾼: 1.0, 體積: 1.0, 材質: C 
# 長: 2.0, 寬: 2.0, ⾼: 2.0, 體積: 8.0, 材質: B 
# 長: 3.0, 寬: 3.0, ⾼: 3.0, 體積: 27.0, 材質: A

class Cuboid:
    def __init__(self, length=0.0, width=0.0, height=0.0):
        self.length = length
        self.width = width
        self.height = height
        self.volume = length * width * height

    def getCuboidsInfo(self):
        print(f"長: {self.length}", end = ", ")
        print(f"寬: {self.width}", end = ', ')
        print(f"高: {self.height}", end = ", ")
        print(f"體積: {self.volume}", end = ", ")

class House(Cuboid):
    def __init__(self, length=0.0, width=0.0, height=0.0, material=""):
        super().__init__(length, width, height)
        self.material = material
        
    def getInfo(self):
        super().getCuboidsInfo()
        print(f"材質: {self.material}")

num = int(input(f"請問有幾個長方體? "))
for i in range(num):
    l, w, h, m = list(input(f"請輸入第{i+1}個的長、寬、高(空白間隔): ").split())
    locals()['cuboid'+str(i+1)] = House(int(l), int(w), int(h), m)
print(f"輸入的{num}個長方體資訊如下:")
for i in range(num):
    locals()['cuboid'+str(i+1)].getInfo()