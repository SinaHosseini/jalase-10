
class Time():
    def __init__(self, s, m, h):
        self.second = s
        self.minute = m
        self.hour = h


while True:
    s = int(input("enter second: "))
    if s >= 60:
        print("please enter correct")

    else:
        break

while True:
    m = int(input("enter minute: "))
    if m >= 60:
        print("please enter correct")

    else:
        break

while True:
    h = int(input("enter hour: "))
    if h >= 24:
        print("please enter correct")

    else:
        break


time = Time(s, m, h)

print("time is: ")
print(time.hour, ":", time.minute, ":", time.second)
