# 1. **Tuple Unpacking**: Create a list of tuples, each containing a name and an age. Then, use tuple unpacking to iterate through the list and print each name and age.
    
data= [("Sonu", 25), ("Monu", 30)]
for name, age in data:
    print(f"{name} is {age} years old.", end=" ")

# 1. **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
def pair(dictionary, name, age):
    dictionary[name] = age
    return dictionary
def update_age(dictionary, name, new_age):
    if name in dictionary:
        dictionary[name] = new_age
        return dictionary
    else:
        return f"Name '{name}' not found in the dictionary."
def delete_name(dictionary, name):
    if name in dictionary:
        del dictionary[name]
        return dictionary
    else:
        return f"Name '{name}' not found in the dictionary."
data = {}
print(pair(data, "John", 25))   
print(update_age(data, "John", 26))         
print(delete_name(data, "John"))            


# 1. **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.

def sum(nums, target):
    num_dict = {} 
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        else:
            num_dict[num] = i
    return None
nums = [2, 7, 11, 15]
target = 9
result =sum(nums, target)
print(result)

# 1. **Palindrome Check**: Write a Python function that checks whether a given word or phrase is a palindrome.
def palindrome(word):
    word = word.lower().replace(" ", "")  
    reversed = word[::-1] 
    if word == reversed:
        return True
    else:
        return False
input_word = "madam"
if palindrome(input_word):
    print(f"The word {input_word} is a palindrome.")
else:
    print(f"The word {input_word} is not a palindrome.")


    # 1. **Selection Sort**: Implement the selection sort algorithm in Python.
    
# def selection_sort(arr):
#   n = len(arr)
# for i in range(n - 1):
#         min_index = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
# return arr
# input_list = [64, 25, 12, 22, 11]
# sorted_list = selection_sort(input_list)
# print(sorted_list)


# 1. **Implement Stack using Queue**: Use Python's queue data structure to implement a stack.
   
from queue import Queue
class done:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
    def push(self, data):
        self.queue1.put(data)
    def pop(self):
        if self.queue1.empty():
            return None
        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())
        popped_item = self.queue1.get()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return popped_item

stack = done()
stack.push(1)
stack.push(2)
print(stack.pop())   
stack.push(3)
print(stack.pop())   
print(stack.pop())   


# 1. **FizzBuzz**: Write a Python program that prints the numbers from 1 to 100, but for multiples of three, print "Fizz" instead of the number, for multiples of five, print "Buzz", and for multiples of both three and five, print "FizzBuzz".
   
def fizz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)
for i in range(1, 101):
    print(fizz(i), end=", ")


# 1. **File I/O**: Write a Python program that reads a file, counts the number of words, and writes the count to a new file.

def count(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read()
        word_count = len(text.split())
    with open(output_file, 'w') as file:
        file.write(f"Number of words: {word_count}")
input = "input.txt"
output= "output.txt"
count(input, output)


# 2. **Exception Handling**: Write a Python function that takes two numbers as inputs and returns their division, handling any potential exceptions (like division by zero).
 
def numbers(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."
num1 = 5
num2 = 0
result = numbers(num1, num2)
print(result)