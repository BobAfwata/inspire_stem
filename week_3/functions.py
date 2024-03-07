
#define function
def print_name():
    print(" My name is Bob Afwata")


#calling the function
#print_name()

def print_details(name , age, id, gender):
    print("I am {0} , {1} years old . My Id no is {2} and gender is {3} ".format(name , age, id, gender))


print_details("Bob Afwata" ,"24","29009189", "male")
print_details("Lucy Lui" ,"48","19089189", "female")

def sum_nums(x,y):
    return x + y

def prod_numbers(x,y):
    return x * y 
    

z = sum_nums(10,20)
print(z)
print(prod_numbers(5,16))


def print_odds(first_no, last_number):
    for i in range(first_no, last_number):
        print(i % 2 )

print_odds(0,15)

function to print all prime no btn 1 - 99
function to calcuate sa of cylinder, cone, cube, sphere , volume of 4 
function to print all squares , cubes of no btn 1 - 10