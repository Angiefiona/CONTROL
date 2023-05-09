# Write a Python program that takes a list of strings as input and outputs the number of times 
# each string appears in the list, using a dictionary and conditional statements.
strings = {"Tasha", "Fiona", "Angela", "Tanet", "Robert", "Tasha"}
output = {}
for string in strings:
    if string in output:
        output[string] +=1
    else:
        output[string] = 1     
for string, count in output.items():
    print(f"{string}: {count}")

# Write a Python program that takes a list of numbers as input and outputs the median of the numbers 
import statistics
digits =  [2,4,6,8,10,12,14]
median  = statistics.median(digits)
print(median)

# Write a Python program that takes a list of numbers as input and outputs 
# the second largest number in the list using conditional statements and a for loop.
largest = num_list[0]
second_largest = num_list[0]
for num in num_list:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print("The second largest number in the list is:", second_largest)
numbers = [8,9,5,2,1,7] 

# Write a Python program that takes a year as input and determines if it is a leap year.
year = input("enter a year")
if year % 4 == 0:
    if year % 100 ==0:
     print(year, "Is a leap year")
else:
    print(year, "not a leap year")
year = [2000, 2014, 2018, 2023]
# Write a Python program that takes a string as input and
#  checks if it is a palindrome (reads the same forwards and backwards), 
# ignoring spaces and punctuation.strings = ["apple", "banana", "apple", "orange", "banana", "apple"]

def palindrome(str):
    str = str.replace(" ", "")
    reversed_word = str[::-1]
    if str == reversed_word:
        return True
    else:
        return False