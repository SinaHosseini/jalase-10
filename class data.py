
class Data():
    def __init__(self, d, m, y):
        self.day = d
        self.month = m
        self.year = y


d = int(input("please enter day: "))
m = int(input("please enter month: "))
h = int(input("please enter year: "))

data = Data(d, m, h)

print("data is: ")
print(data.year, "/", data.month, "/", data.day)
