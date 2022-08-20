from typing import Dict, List

def getNumber():
    number = input('Enter a number: ')
    try:
        if not number.isnumeric():
            raise ValueError('Only numbers are allowed')
        return int(number)
    except ValueError as ve:
        print(ve)
        return False

def validateNumber(number: int) -> bool:
    is_prime: bool = False
    prime_numbers: List[int] = [value for value in range(2, number) if number % value == 0]
    primes: int = len(prime_numbers)
    if primes == 0:
        is_prime = True
    return is_prime


def run():
    number = getNumber()
    if number:
        if validateNumber(number):
            print('The number entered is prime')
        else:
            print('The number entered is not prime')

if __name__ == '__main__':
    run()