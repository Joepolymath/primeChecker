
# to check for a prime number: METHOD 1
# A prime number is a number that can be divided by itself or 1
# even numbers cannot be prime
# assuming the number is 7
def isPrime(num):
   if num % 2 == 0:
      return False
   
   else:
      for i in range(2, num):
         if num % i == 0:
            return False
      return True

# print(isPrime(99))

# another implementation: METHOD 2
# num = 6
def isPrime2(num):
   if num % 2 == 0:
      return False
   else:
      for i in range(3, num, 2):
         if num % i == 0:
            return False
      return True

print(isPrime2(99))

# an even better implementation: METHOD 3
def isPrime3(num):
   if num % 2 == 0:
      return False
   
   else:
      divisorRange = None
      if num > 10:
         divisorRange = range(3, 10, 2)
      else:
         divisorRange = range(3, num, 2)
      
      for i in divisorRange:
         if num % i == 0:
            return False
      
      return True

# print(isPrime3(99))