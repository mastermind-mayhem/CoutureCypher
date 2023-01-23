# D.Couture
# 1/11/2023
# Information for cypher

import time

def info():
    input("""
    More information on the Couture Cypher:

    This is a two step encryption that requires two keys
    
    --- For next press enter
    """)
    time.sleep(1.5)
    input("""
    1. - The first step is to create the key, we need to use a simple math equation to calculate the approximate amount of seconds since the year 0000
    It gets an eleven digit number, we then take the number and take each second letter and bring it down to a number in between 26
    | 64 23 47 25 65 7 |

    | 12 23 21 25 13 7 |

    We can then take the numbers and change it to the letters of the alphabet, i.e. 1 is a, 2 is b, etc

    | L  W  U  Y  M  G |

    This is now our key

    --- For next press enter
    """)
    time.sleep(1.5)

    input("""
    2. - Use the key (LWUYMG) and swap the common letters in the english language (EARIOT) in the users input mark them with a symbol ($) and then attach the key to the front

    User input -----
    | Hello World |

    | Hl$llm$ Wm$u$ld |

    --- For next press enter
    """)
    time.sleep(1.5)

    input("""
    3. - Create the second key using the average between the current minute and second and getting it 

    Current time ---
    | 5:45:37 |

    In this case it is 45 and 37 which the average is 41 we then subtract 26 from it to make sure it can be tranfered into a letter
    We end up with 15
    this means that if our first letter was an "A" then it goes to an O
    Shifting all the letters to the right with the key and afterwards we attach the key to the front in letter form so you get something completely unreadable as an output

    --- For next press enter
    """)
    time.sleep(1.5)

    input("""
    4. - This code is virtually impossible to crack by hand because of the unique keys. For the keys there is Approximately 8 Billion different key combinations, 
    so if you knew how the encryption worked and you tried 4000 different combinations a day then it would take you 55 thousand years to find the answer
    so if we encrypted this and separated the keys it would make it almost impossible to crack

    For more information on:

    How I switch between letters and numbers
    https://www.digitalocean.com/community/tutorials/python-ord-chr

    How the second step of the encryption works
    https://en.wikipedia.org/wiki/Caesar_cipher

    --- Press enter to exit information
    """)