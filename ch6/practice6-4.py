class Station:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon
    
    def show(self):
        print(f"站名: {self.name}, 緯度: {self.lat}, 經度: {lon}")
    
    def __eq__(self, other):
        return self.name == other.name
    
    @staticmethod
    def showAll(stations):
        for station in stations:
            station.show()
stat_list = []
while True:
    name = input(f"站名: ")
    lat = float(input(f"緯度: "))
    lon = float(input(f"經度: "))
    stat  = Station(name, lat, lon)
    if stat in stat_list:
        print(f"{stat.name}站已經存在")
        continue
    else:
        stat_list.append(stat)
    stat.show()
    ans = input(f"繼續輸入(Y|y): ")
    if ans == 'Y' or ans == 'y':
        continue
    else:
        break
print(f"車站依照緯度高到低排序如下:")
Station.showAll(sorted(stat_list, key=lambda stat: stat.lat, reverse=True))

    