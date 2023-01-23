from coutureCypher import *

def test_translatetonum():
    print('Letters to Numbers: ', end='\a')
    inst = cypher('Hello World')
    try:
        num = inst._translatetonum('a')
        if num == 0:
            print('Passed')
        else:
            print('Failed ----')
            print('Returned {}'.format(num))
    except Exception as error:
        print('Test Failed')
        print(error)

def test_changeletter():
    print('Round Down to Letter: ', end='\a')
    inst = cypher('Hello World')
    try:
        letter = inst._changeletter(97)
        if letter == "t":
            print('Passed')
        else:
            print('Failed ----')
            print('Returned {}'.format(letter))
    except Exception as error:
        print('Test Failed')
        print(error)

def test_keyseconds():
    print('Key Minute Second Average: ', end='\a')
    inst = cypher('Hello World')
    try:
        key = inst._keyseconds()
        if len(key) == 1 and ord(key) >= 97 and ord(key) <= 122:
            print('Passed')
        else:
            print('Failed ----')
            print('Returned {}'.format(key))
    except Exception as error:
        print('Failed')
        print(error)

def test_keyworldseconds():
    print('Key World Seconds 00: ', end='\a')
    inst = cypher('Hello World')
    try:
        key = inst._keyworldseconds()
        try:
            key = int(key)
            print('Failed ----')
            print('Returned {}'.format(key))
        except:
            if len(key) == 6:
                print('Passed')
            else:
                print('Failed ----')
                print('Returned {}'.format(key))
    except Exception as error:
        print('Failed')
        print(error)

test_translatetonum()
test_changeletter()
test_keyseconds()
test_keyworldseconds()