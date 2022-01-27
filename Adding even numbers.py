#Addition of all the even numbers from 1 to 100  

total = 0
for number in range(1,101):
    if number % 2 == 0:
        total += number
print(total)

#for num in range(1,101,2):
    #total += number
#print(num)
#above code gives odd numbers

#for num in range(2,101,2):
    #print(num)
#even numbers 
