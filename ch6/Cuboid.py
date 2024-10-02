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