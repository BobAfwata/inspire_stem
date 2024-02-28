laptop = {"make":"Lenovo", "color": "black","weight":"1.2",
          "year" : "2020"}


print(laptop["make"])
print(laptop["color"])
print(laptop["year"])

# change the values in a dictionary
laptop["color"] = "red"
laptop["year"] = "2009"

print(laptop)


laptop["size"] = "1200mm x 600mm"
print(laptop)

del laptop["color"]

print(laptop)

siz_laptop = laptop.copy()

print(siz_laptop)


"""
for key,value in laptop.items():
    print(key)
    print("\n")
    print(value)
"""


