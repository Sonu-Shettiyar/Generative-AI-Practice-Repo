# 1. Write a Python program that prints "Hello, World!" to the console.

print("Hello, World!")

# 2.  Create variables of each data type (integer, float, string, boolean, list, tuple, dictionary, set) and print their types and values.

integervar = 10
floatvar = 3.14
stringvar = "Hello, Python!"
booleanvar = True
listvar = [1, 2, 3, 4, 5]
tuplevar = (10, 20, 30)
dictionaryvar = {"name": "John", "age": 25, "city": "New York"}
setvar = {1, 2, 3, 4, 5}

print(f"Type of integervar: {type(integervar)}, value: {integervar}")
print(f"Type of floatvar: {type(floatvar)}, value: {floatvar}")
print(f"Type of stringvar: {type(stringvar)}, value: {stringvar}")
print(f"Type of booleanvar: {type(booleanvar)}, value: {booleanvar}")
print(f"Type of listvar: {type(listvar)}, value: {listvar}")
print(f"Type of tuplevar: {type(tuplevar)}, value: {tuplevar}")
print(f"Type of dictionaryvar: {type(dictionaryvar)}, value: {dictionaryvar}")
print(f"Type of setvar: {type(setvar)}, value: {setvar}")


# 3.  Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.
  
numberslist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numberslist.append(20)

numberslist.remove(3)

numberslist.sort()

print(numberslist)

# 4. Write a Python program that calculates and prints the sum and average of a list of numbers.

def calculatesumandaverage(numbers):
    sumofnumbers = sum(numbers)
    
    averageofnumbers = sumofnumbers / len(numbers)
    
    return sumofnumbers, averageofnumbers

inputlist = [10, 20, 30, 40]

sumresult, averageresult = calculatesumandaverage(inputlist)

print(f"Sum: {sumresult}, Average: {averageresult}")


# 5. Write a Python function that takes a string and returns the string in reverse order.
   
def reversestring(inputstring):
    reversedstring = ""
    for char in inputstring[::-1]:
        reversedstring += char

    return reversedstring
inputstring = "Python"
outputstring = reversestring(inputstring)

print(outputstring)

# 6. Write a Python program that counts the number of vowels in a given string.
    
def countvowels(inputstring):
    vowels = set("aeiouAEIOU")
    count = 0
    for char in inputstring:
        if char in vowels:
            count += 1

    return count

inputstring = "Hello"
vowelcount = countvowels(inputstring)
print(f"Number of vowels: {vowelcount}")


# 7.  Write a Python function that checks whether a given number is a prime number.

def isprime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True
inputnumber = 13
if isprime(inputnumber):
    print(f"{inputnumber} is a prime number.")
else:
    print(f"{inputnumber} is not a prime number.")

# 8.  Write a Python function that calculates the factorial of a number.

def factorial(number):
    if number == 0:
        return 1
    else:
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result
inputnumber = 5
factorialresult = factorial(inputnumber)
print(f"Factorial of {inputnumber} is {factorialresult}.")


# 9. Write a Python function that generates the first n numbers in the Fibonacci sequence.
  
def fibonacci(n):
    fibonaccisequence = [0, 1]

    if n <= 2:
        return fibonaccisequence[:n]

    while len(fibonaccisequence) < n:
        nextnumber = fibonaccisequence[-1] + fibonaccisequence[-2]
        fibonaccisequence.append(nextnumber)

    return fibonaccisequence
n = 5
fibonaccisequence = fibonacci(n)
print(fibonaccisequence)


# 10. Use list comprehension to create a list of the squares of the numbers from 1 to 10.

squareslist = [x**2 for x in range(1, 11)]
print(squareslist)