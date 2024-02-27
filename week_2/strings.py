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

# printing a string 

activity = "dancing"
print("My hobby is %s" %(activity))

# printing a float 

height = 1.2334909 
print("My height is  %5.3f"% (height))

# printing an integer 
age = 32
print("My age is  %d"% (age))


name = "Bob Afwata"
print(len(name))

print(f"My full name is {name }")


course = "Electrical"
school = "Engineering"

print(" I am studying {course} in the school of {school}" .format(course = "Medicine",school="Human Sciences"))