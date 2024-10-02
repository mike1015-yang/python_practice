# 承襲 6-1，不過改成可以輸入多個長⽅體資訊，所以 Cuboid 類別新增⼀個static⽅法  
# getCuboidsInfo(cuboid)：回傳所有長⽅體資訊  
# 主流程 
# 詢問使⽤者欲輸入的長⽅體總個數 
# 讓使⽤者輸入指定個數的長⽅體資訊，並顯⽰所有輸入長⽅體的長、寬、⾼與體積
# 請問有幾個長⽅體? 3 
# 請輸入第1個長⽅體的長、寬、⾼(空⽩間隔): 1 1 1 
# 請輸入第2個長⽅體的長、寬、⾼(空⽩間隔): 2 2 2 
# 請輸入第3個長⽅體的長、寬、⾼(空⽩間隔): 3 3 3 
# 輸入的3個長⽅體資訊如下: 
# 長: 1.0, 寬: 1.0, ⾼: 1.0, 體積: 1.0 
# 長: 2.0, 寬: 2.0, ⾼: 2.0, 體積: 8.0 
# 長: 3.0, 寬: 3.0, ⾼: 3.0, 體積: 27.0

class Cuboid:
    volume = 1
    def __init__(self, length=0.0, width=0.0, height=0.0):
        self.length = length
        self.width = width
        self.height = height
    @staticmethod
    def getCuboidsInfo(cubCls, cubObj):
        print(f"長: {cubObj.length}", end = ", ")
        print(f"寬: {cubObj.width}", end = ', ')
        print(f"高: {cubObj.height}", end = ", ")
        cubCls.volume = cubObj.length * cubObj.width * cubObj.height
        print(f"體積: {cubCls.volume}")

num = int(input(f"請問有幾個長方體? "))
for i in range(num):
    l, w, h = list(map(float, input(f"請輸入第{i+1}個的長、寬、高(空白間隔): ").split()))
    locals()['cuboid'+str(i+1)] = Cuboid(l, w, h)
print(f"輸入的{num}個長方體資訊如下:")
for i in range(num):
    Cuboid.getCuboidsInfo(Cuboid, locals()['cuboid'+str(i+1)])