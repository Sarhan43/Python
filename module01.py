def factors(num) :
    '''
    this function takes in a number and returns its factors as a list
    '''

    factor_ = []
    for i in range (1,num+1):
      if num%i==0:
        factor_.append(i)
    return factor_


def fact_sum(number):
  '''
    this method accepts the factors of a number in the form of a list and finds the sum of all the factors and returns the sum .
     Eg fact_sum(10)
     >>  8
  '''
  fact = factors(number)
  sum_of_factors = 0
  for i in fact [:-1]:
    sum_of_factors = sum_of_factors + i
  return sum_of_factors,fact

def add(num1,num2):
    ''' this methods add two numbers and prints their sum '''
    print(f"the sum of {num1} and {num2} is (num1+num2)")
def isPrime(num):
    '''
    This method finds if the given number is prime or not and Returns true for prime false for not 
    ex : isPrime(7)
    >> True 
    '''
    count = 0
    for i in range  (1,num+1):
          if num%i == 0:
              count+=1
    if count > 2:
              return False
    else :
              return True



def perfect_number(low,high):
    '''
    This function accepts a range  as (low,high) and it'll calculate what are the perfect numbers in that particular range

    Note : A perfect number is that number where when we add all the functio of the number excluding number its-self , the sum is equal to the number itself

    Eg : if the number is 6. factors of 6 = [1,2,3,6]
    sum of all factors excluding number itself = 1+2+3
    number = 6
    hence 6 is a perfect number
   '''
    from functools import reduce

    perfect = []
    for num in range(low,high+1):
        fact = factors(num)
        print(fact)
        fact_sum = reduce(lambda x,y : x+y,fact[:-1])
        if fact_sum == num :
            perfect.append(num)
    if len(perfect)==0:
        print('There are no perfect numbers in the given range({low},{high})'.format(low=low,high=high))
    else :
         perfect = [str(i) for i in perfect]
         perfect = ','.join(perfect)
         print(f'The perfect numbers in the given range({low},{high}) are {perfect}')

def Calci(op, x, y):
    """
    Performs a simple calculation based on the provided operator and two numbers.

    Args:
        op: The operation to perform ('+', '-', '*', '/').
        x: The first number.
        y: The second number.

    Returns:
        The result of the calculation, or an error message if the operation
        is invalid or division by zero is attempted.
    """
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            return "Error: Division by zero"
        return x / y

    if op == '+':
        result = add(x, y)
    elif op == '-':
        result = subtract(x, y)
    elif op == '*':
        result = multiply(x, y)
    elif op == '/':
        result = divide(x, y)
    else:
        result = "Invalid operator"

    return result
