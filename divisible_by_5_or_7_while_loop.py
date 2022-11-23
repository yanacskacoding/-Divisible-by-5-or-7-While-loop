'''Instructions:
Write a program that asks a user to enter a number and print out how many numbers from 1 to N (including N) are divisible by 5 or 7 and the list of the numbers using while loop.

Example:
>>>
40                                                                  
There are 12 numbers divisible by 5 and 7.
5,7,10,14,15,20,21,25,28,30,35,40,        
 '''

def divisible(num):
    if int(num):
        if (int(num) / 5).is_integer() or (int(num) / 7).is_integer():
            return True
    return False

def remove_special_chars(thisString):
    return (''.join(e for e in thisString if e.isalnum()))

def check_int(num):
    if num.isdigit():
        return int(num)
    else:
        print("Input is not a number!")
        exit(1)


num = input()
num = remove_special_chars(num)
num = check_int(num)

numbers = []
thisNum = 1

while thisNum != int(num)+1:
    if divisible(int(thisNum)):
        numbers.append(int(thisNum))
    thisNum += 1

print(numbers)
print("There are", len(numbers), "numbers divisible by 5 or 7" )