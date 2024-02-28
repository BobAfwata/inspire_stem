friends = ["Jane","Lucy","Mary","Dan","Susan"]

for friend in friends:
    print(friend)

enemies = friends[:]  # copy one list into another 
print(enemies)

fruits = ["Guava","Lemon","Mango","lime","strawberry","pineapple"]

#slice the list ie get part of the list 

print(fruits[0:3])

del fruits[0]

print(fruits)

squares = [] # initializes an empty list 

for x in range(0,11):
    squares.append(x**2)

print(squares)



