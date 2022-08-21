from typing import Dict

def getWord():
    word = input('Enter a word: ')
    try:
        if not word.isalpha():
            raise ValueError('Only words are allowed')
        return word
    except ValueError as ve:
        print(ve)
        return False

def getRepeat():
    repeat = input('How many times do you want to repeat the word?: ')
    try:
        if not repeat.isnumeric():
            raise ValueError('Only numbers are allowed')
        return repeat
    except ValueError as ve:
        print(ve)
        return False

def getValues() -> Dict:
    values: Dict[str, str] = {}
    word = getWord()
    repeat = getRepeat()
    if word and repeat:
        values = {
            'word': word,
            'repeat': repeat
        }
    return values

def stringRepeat(word: str):
    def repeat(number: int):
        return word*number
    return repeat

def run():
    data = getValues()
    if len(data) != 0:
        word = data['word']
        repeat = int(data['repeat'])
        word_repeat = stringRepeat(word)
        print(word_repeat(repeat))
    else:
        print('Wrong data')

if __name__ == '__main__':
    run()