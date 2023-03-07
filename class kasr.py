
class Fraction():
    def __init__(self, s, m):
        self.sorat = s
        self.makhraj = m


s = int(input("please enter sorat: "))
m = int(input("please enter makhraj: "))

kasr = Fraction(s, m)
print()
print(kasr.sorat)
print("---")
print(kasr.makhraj)
