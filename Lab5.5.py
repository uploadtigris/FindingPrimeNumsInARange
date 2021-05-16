######################################################
#
#   This program ask the user for a range of
#   numbers and returns a list of prime
#
#   Author:  Tigris Mendez
#
#   Date:    April 10, 2021
#
#   Version: 5.5
#
######################################################


# Welcome Statement
print("Hello User! Welcome to the PrimeNumbersInARangeFinder 2000. Clever name right? ;) "
      "The goal of this program is to find every prime within the range of two given numbers.")

import math

# intilize a list to hold prime numbers
a = []


# define function is_prime to dtermiine if integer in is prime, and return true if prime.
def is_Prime(n):
    if n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False
    elif n == 1:
        return False
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    print("error in is_prime")


# Gets values and ensures that inputed integers are sequencial positive real numbers
def get_Nums():
    n = int(input("Enter first number in range:"))
    n2 = int(input("Enter the last number in range:"))
    if n2 > n:
        final_int = n2
        first_int = n
    elif n > n2 or n < 0 or n2 < 0:
        print("error: first integer must be less than second")
        quit()
    b = [first_int, final_int]
    return b


# define function main whose purpose is to full list "a" with prime numbers within the inputed range
def main():
    f = get_Nums()
    for i in range(f[0], f[1]):
        if is_Prime(i):
            a.append(i)
    print(a)


main()
