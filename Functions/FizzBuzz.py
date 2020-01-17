"""
Write a program that prints the numbers from 1 to 100.
But for multiples of three print "Fizz" instead of the
number and for the multiples of five print "Buzz". For
numbers which are multiples of both three and five print
"FizzBuzz".
"""

# My Solution
def counter(max_value):
    for num in range(1, max_value):
        if num % 3 == 0 and num % 5 != 0:
            print('Fizz')
        elif num % 3 != 0 and num % 5 == 0:
            print('Buzz')
        elif num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        else:
            print(num)


counter(101)

# JH Solution
def fizz_buzz(max_num):
  for num in range(1, max_num + 1):
    if num % 3 == 0 and num % 5 == 0:
      print('FizzBuzz')
    elif num % 5 == 0:
      print('Buzz')
    elif num % 3 == 0:
      print('Fizz')
    else:
      print(num)


fizz_buzz(100)