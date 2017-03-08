def is_prime_number(n):
	""" find range of prime numbers between 0 and input number(n) from user"""
n = int(input("Enter upper range: ")) # ensures an integer only is entered
for num in range(0,n + 1): #from 0 to n
   
   if num > 1: # prime numbers are greater than 1 so numbers 0 and negative numbers won't work
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
print("Prime numbers between",0,"and",n,"are:")
