# strings in python
# Date 
# Name : Bob

city = "nairobi"

print(city[0]) # n
print(city[1]) # a
print(city[2]) # i
print(city[3])
print(city[4])
print(city[-1])
print(city[-2]) # i

# convert to uppercase
print(city)
print("\n") # prints a new line
print(city.upper())
name = "BOB AFWATA"
print(name) 
print(name.lower()) # converts string to lower case
town = "      Naivasha     "
print(town)
print("\t") # new tab
print(town.strip())

# add two strings 

f_name = "Joyce"
s_name = "Waithera"

full_name = f_name + s_name

print(full_name)


#replacing a character 

fruit = "OrangeOOOOOO"

print(fruit.replace("O","Y"))

subject = "Physical:Sciences"

print(subject.split(":"))

age = 30 
height = 1.2 

print("I am  {0} years old  and {1} meters tall " .format(age,height))

