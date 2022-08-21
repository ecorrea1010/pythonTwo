from typing import Dict

def getValues():
    numbers: Dict[str, int] = {}
    number = input('Enter a number: ')
    divisor = input('By how much do you want to divide the number: ')
    try:
        if not number.isnumeric() or not divisor.isnumeric():
            raise ValueError('Wrong data, Only numbers are allowed')
        numbers = {
            'number': int(number),
            'divisor': int(divisor)
        }
        return numbers
    except ValueError as ve:
        print(ve)
        return False

def makeDivisor(number: int):
    return lambda x: x / number

def run():
    data = getValues()
    if data:
        number = data['number']
        divisor = data['divisor']
        division = makeDivisor(divisor)
        print(division(number))

if __name__ == '__main__':
    run()