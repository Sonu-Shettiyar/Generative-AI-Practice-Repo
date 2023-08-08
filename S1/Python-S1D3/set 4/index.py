# 1. **Anagram Check**: Write a Python function that checks whether two given words are anagrams.
 
def anag(word1, word2):
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    return sorted(word1) == sorted(word2)
word1 = "sonu"
word2 = "monu"
result =anag(word1, word2)
print(result)

# 2. **Bubble Sort**: Implement the bubble sort algorithm in Python.
    
def cons(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
input [64, 34, 25, 12, 22, 11, 90]
sorted= cons(input)
print(sorted)


# 3. **Longest Common Prefix**: Given a list of strings, find the longest common prefix.

def cons(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for string in strs[1:]:
        i = 0
        while i < len(prefix) and i < len(string) and prefix[i] == string[i]:
            i += 1
        prefix = prefix[:i]
    return prefix
input = ["flower", "flow", "flight"]
result = cons(input)
print(result)


# 4. **String Permutations**: Write a Python function to calculate all permutations of a given string.
#     - 

def cons(s):
    if len(s) == 1:
        return [s]
    perms = []
    for i in range(len(s)):
        first_char = s[i]
        rest_chars = s[:i] + s[i+1:]
        rest_perms = cons(rest_chars)
        for perm in rest_perms:
            perms.append(first_char + perm)
    return perms
input = "abc"
result = cons(input)
print(result)


# 6. **Missing Number**: Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
  
def cons(nums):
    n = len(nums)
    sum = n * (n + 1) // 2
    array_sum = sum(nums)
    num = sum - array_sum
    return num
input = [3, 0, 1]
result = cons(input)
print(result)

# 7. **Climbing Stairs**: You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
   
def cons(n):
    if n == 0:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
res = 3
result = cons(res)
print(result)