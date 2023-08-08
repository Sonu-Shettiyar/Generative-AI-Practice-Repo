# Write a program to print the following number pattern using a loop.

# Function to print the number pattern
def print_number_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print(i, end=" ")
        print()
num_rows = 5
print_number_pattern(num_rows)


# Write a program to display only those numbers from a [list] that satisfy the following conditions

# - The number must be divisible by five
# - If the number is greater than 150, then skip it and move to the next number
# - If the number is greater than 500, then stop the loop


def display_numbers(numbers):
    for num in numbers:
        if num > 500:
            break
        if num % 5 == 0:
            if num > 150:
                continue
            print(num)

numbers = [12, 75, 150, 180, 145, 525, 50]
display_numbers(numbers)


#  **Append new string in the middle of a given string**

# Given two strings, `s1` and `s2`. Write a program to create a new string `s3` by appending `s2` in the middle of `s1`.

def append_middle(s1, s2):
    middle_index = len(s1) // 2
    s3 = s1[:middle_index] + s2 + s1[middle_index:]
    return s3
s1 = "Ault"
s2 = "Kelly"

s3 = append_middle(s1, s2)
print(s3)


#  **Arrange string characters such that lowercase letters should come first**

# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

def arrange_lowercase_first(input_str):
    lowercase_letters = [char for char in input_str if char.islower()]
    uppercase_letters = [char for char in input_str if char.isupper()]
    result_str = "".join(lowercase_letters + uppercase_letters)
    return result_str

str1 = "PyNaTive"
output_str = arrange_lowercase_first(str1)

print(output_str)


#  **5.Concatenate two lists index-wise**
# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

def add_lists(list1, list2):
    new_list = []
    min_len = min(len(list1), len(list2))
    for i in range(min_len):
        new_list.append(list1[i] + list2[i])
    if len(list1) > len(list2):
        new_list.extend(list1[min_len:])
    else:
        new_list.extend(list2[min_len:])

    return new_list
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
result = add_lists(list1, list2)
print(result)


### **6: Concatenate two lists in the following order**
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
concatenate= list1 + list2
print(concatenate)


### **7: Iterate both lists simultaneously**
# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for item1, item2 in zip(list1, reversed(list2)):
    print(item1, item2)


### **8: Initialize dictionary with default values**
# In Python, we can initialize the keys with the same values.

employ = ['Kelly', 'Emma']
post = {"designation": 'Developer', "salary": 8000}
employ_data = {employ: post for employ in employ}
print(employ_data)


### **9: Create a dictionary by extracting the keys from a given dictionary**
# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

list = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
keys = ["name", "salary"]
new_list = {key: list[key] for key in keys}

print(new_list)

### **10: Modify the tuple**
# Given a nested tuple. Write a program to modify the first item (22) of a list inside the following tuple to 222

# tuple1 = (11, [22, 33], 44, 55)
# modified_list = list(tuple1)
# modified_list[1][0] = 222
# modified_tuple = tuple(modified_list)
# print(modified_tuple)