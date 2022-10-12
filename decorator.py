def withDecorator(func):
    def wraper(*args, **kwargs):
        func(*args, **kwargs)
    return wraper

@withDecorator
def setValues(name: str, characteristic: str):
    print('I am '+name+', I am a '+characteristic)

def run():
    name = input('Enter a name: ')
    characteristic = input('Enter a characteristic: ')
    setValues(name, characteristic)

if __name__ == '__main__':
    run()