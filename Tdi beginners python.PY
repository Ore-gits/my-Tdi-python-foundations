"""1. Create a variable “x” and assign it the integer value “10”. Create another variable “y” and 
assign it the float value “20.5”. Write a Python statement to add these two variables and 
print the result."""
X =  10
Y = 20.5
SUM = X + Y
print(SUM)

"""Create a variable “name” and assign it your name as a string. Write a Python statement 
to print the length of this string."""
Name = "Oreoluwa"
print(Name)

""" Write a Python function called “calculate_area” that takes the length and width of a 
rectangle as arguments and returns the area. Test the function with a length of “5” and a 
width of “3”."""
def calculate_area(length,width):
    area = length * width
    print(f'The calculated area id {area}')

calculate_area(5,3)

"""Given two variables, “a = 15” and “b = 4”, write Python code to compute and print the 
result of integer division and modulus operation."""
a = 15
b = 4
print(a//b)
print(a%b)

""" Write a Python statement to check if a variable “age” is greater than or equal to “18” and 
less than “65”. Print "Adult" if the condition is true, otherwise print "Not an Adult".
"""
age = 56
if age >= 18 and age <= 65:
    print("Adult")
else:
    print("Not an Adult")

"""6.Create two variables, “num1 = 12” and “num2 = 15”. Write a Python statement to check if 
“num1” is not equal to “num2” and print the result.
"""
num1 = 12
num2 = 15
print(num1 == num2)

"""7. Write a Python function called “is_even_and_positive” that takes an integer as input and 
# returns “True” if the number is both even and positive, otherwise returns “False”."""
def is_even_and_positive(num):
    if num % 2 == 0:
            print(True)
    else: print(False)

is_even_and_positive(45)

"""Given two boolean variables, “x = True” and “y = False”, write a Python statement to 
compute and print the result of the logical “AND” and “OR” operations."""
x = True
y = False
if x and y is True: 
    print('AND')
else: 
    print('OR')

"""9. Write a Python function called “greet” that takes a name as an argument and prints a 
greeting message like "Hello, [name]!". Call this function with your name."""
def greet(name):
    print(f'Hello, hi there my name is {name}')
greet('Oreoluwa')

""" 10.Create a Python function “find_max” that takes a list of numbers as input and returns 
the maximum number in the list. Test the function with the list “[3, 7, 2, 5, 9]”."""
def find_max(*lists):
    digit = []
    for i in lists:
        digit.append(i)
    return max(digit)
print(find_max(3, 7, 2, 5, 9))

""". Write a Python statement to find and print the type of the variable “x” where “x = [1, 2, 
3]”."""
x = [1, 2, 3]
print(type(x))

""" Create a list of numbers “[4, 2, 9, 1]” and use an inbuilt function to sort this list in 
ascending order. Print the sorted list."""
y = [4, 2, 9, 1]
print(sorted(y))

""" Write a Python function called “calculate_discount” that takes the original price and 
discount percentage as arguments, calculates the discounted price, and returns it. Test the 
function with a price of “100” and a discount of “15”."""
def calculate_discount(Original_price,discount_Percentage):
    amount = Original_price * (discount_Percentage/100)
    discount = Original_price - amount
    return discount
print(calculate_discount(100,15))

    
"""Write a Python script that prompts the user to enter their age and prints whether they 
are a minor (age < 18) or an adult (age >= 18). Use comparison and logical operators in your 
solution.""" 
user = 'Oreoluwa'
age = int(input(f'{user}, please enter your Age:' ))
if age < 18 :
    print(f'Dear {user}, your age is {age} years this means you are a minor')
else: print(f'Dear {user}, your age is {age} years this means you are an adult')

"""Create a function called “string_statistics” that takes a string as input and returns a 
tuple containing the length of the string, the string in uppercase, and the string in 
lowercase. Test the function with the string "Python Programming"."""
def string_statistics(statement):
    string_length = len(statement)
    string_upper = statement.upper()
    string_lower= statement.lower()
    return string_length, string_upper, string_lower
print(tuple(string_statistics('Python Programming')))