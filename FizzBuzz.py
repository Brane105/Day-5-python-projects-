#your program should print each number from 1 to 100 in turn 
for number in range(1,101):
  #number divisible by 3 and 5 will give FizzBuzz
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
  #number divisible by 3 will give Fizz
    elif number % 3 == 0:
        print("Fizz")
  #number divisible by 5 will give buzz 
    elif number % 5 == 0:
        print("Buzz")
  #none of them number is divisible by either 3,5 it return the same number 
    else:
        print(number)
