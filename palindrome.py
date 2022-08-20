def getWord() -> str:
    word = input('Enter a word: ')
    try:
        if not word.isalpha():
            raise ValueError('It is a not word')
        return word.replace(' ', '').lower()
    except ValueError as ve:
        print(ve)
        return False

def validateWord(word: str) -> bool:
    return word == word[::-1]

def run():
    word = getWord()
    if word:
        if (validateWord(word)):
            print('The word entered is a palindrome')
        else:
            print('The word entered is not a palindrome')

if __name__ == '__main__':
    run()