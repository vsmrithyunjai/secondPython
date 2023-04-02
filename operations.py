name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something else
    print("True")
else:
    # do another thing
    print("False")

print(not False) # Prints out True
print((not False) == (False)) # Prints out False

# change this code
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")

#The following values in Python are false in the context of if and other logical contexts:
#False
#None
#numeric values equal to 0, such as 0, 0.0, -0.0
#empty strings: '' and u''
#empty containers (such as lists, tuples and dictionaries)
#anything that implements __bool__ (in Python3) to return False, 
#   or __nonzero__ (in Python2) to return False or 0.
#anything that doesn't implement __bool__ (in Python3) 
#   or __nonzero__ (in Python2), but does implement __len__ to return a value equal to 0