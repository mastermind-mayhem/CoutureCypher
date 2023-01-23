# D.Couture
# 12/22/22
# Introduction to Programming - Final

import time
from datetime import date
import subprocess
import coutureCypher_info as info
try:
    import pyperclip
    paperclip = True
except:
    print('Don\'t worry, I am just installing the needed modules')
    time.sleep(3)
    subprocess.run('pip install pyperclip')
    try:
        import pyperclip
        paperclip = True
    except:
        paperclip = False


class cypher:
    # Creates first instance of the class with the user's input
    # init is activated when the class is first called
    def __init__(self, usrinput):
        # this just assigns the user's input to a local variable
        self.usrinput = usrinput

    # The function to translate between numbers and the ascii alphabet
    def _translatetonum(self, key):
        # Ord takes the ascii numeric value of a letter (how many symbols in is the ascii alphabet)
        key = ord(key)
        # 98 is the first letter in the alphabet "a"
        key -= 97
        return key
    
    # Change a random number found 0 - 99 to be less than 26 so that it can translate to a letter later
    def _changeletter(self, item):
        # while the number is greater than 26 subtract 26
        while item > 26:
            item -= 26

        # Add 97 to make it line up with the first letter in the ascii alphabet
        item += 97

        # Use chr to transfer to ascii
        item = chr(item)
        return item

    # Creates a function to make first encryption key
    def _keyseconds(self):
        # Collect seconds and minutes of the current time
        sec = int(time.strftime("%S", time.localtime()))
        min = int(time.strftime("%M", time.localtime()))

        # average the times
        etime = sec+ min
        etime /= 2

        # Change to acsii
        etime = self._changeletter(int(etime))
        return etime

    # Creates a function to make second encryption key
    def _keyworldseconds(self):
        # Create a date variable for further use
        today = date.today()

        # Collect the exact date down to the second
        sec = int(time.strftime("%S", time.localtime()))
        min = int(time.strftime("%M", time.localtime()))
        hur = int(time.strftime("%H", time.localtime()))
        day = int(today.strftime("%d"))
        mon = int(today.strftime("%m"))
        yer = int(today.strftime("%Y"))

        # Calculate seconds in a unit
        min *= 60
        hur *= 3600
        day *= 86400
        mon *= 2678400
        yer *= 31536000

        # Calculate approximate seconds since year 0000
        totseconds = sec+min+hur+day+mon+yer

        # Transfer seconds by 2 bit chunks into letters using the ascii converter
        # i.e. 40274 --> |40|27|04|
        totseconds = str(totseconds)
        d1 = self._changeletter(int(totseconds[:2]))
        d2 = self._changeletter(int(totseconds[2:4]))
        d3 = self._changeletter(int(totseconds[4:6]))
        d4 = self._changeletter(int(totseconds[6:8]))
        d5 = self._changeletter(int(totseconds[8:10]))
        d6 = self._changeletter(int(totseconds[10:]))

        # Change two bit letters into a six letter string
        key = d1+d2+d3+d4+d5+d6

        # Check for duplicate letters in the string and change to prevent
        key2 = ""
        for letter in key:
            if letter not in key2:
                key2 += letter
            else:
                found = False
                num = ord(letter)
                while found == False:
                    num +=1
                    if chr(num) in key2:
                        continue
                    else:
                        key2 += chr(num)
                        found = True
                    
        # Return the reversed key
        return key2[::-1]

    # Main Encryption program
    def encrypt(self):
        # Create the keys
        key = self._keyworldseconds()
        key1 = self._keyseconds()

        # Create dictionary to transfer the most common letters in the english language to the six letters in the key
        dice = {
            "e": key[0],
            "a": key[1],
            "r": key[2],
            "i": key[3],
            "o": key[4],
            "t": key[5]
        }

        # Set up the user input 
        usrinput = self.usrinput

        # Create empty variable that can be the final result of the first encryption
        imperfect = ""

        # For every letter in the input go through it and replace the letter if it is in common letters
        for input in usrinput:
            if input not in dice:
                imperfect += input
            else: 
                imperfect += dice[input]+"$"

        # take the finished product and add the key to it
        imperfect = key+"^"+imperfect

        # Reverse the numbers
        imperfect = imperfect[::-1]

        # define another finished product
        part = ""

        # for every letter in the new input (key and swapped letters) transfer everything to its new location (caesar cipher)
        for ch in imperfect:
            if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
                newCode = ord(ch) + self._translatetonum(key1)
                if (newCode > ord('z')):
                    newCode -= 26
                part += chr(newCode)
            elif ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
                newCode = ord(ch) + self._translatetonum(key1)
                if (newCode > ord('Z')):
                    newCode -= 26
                part += chr(newCode)
            else:
                part += ch

        # Add the key to the final product
        estring = key1+":"+ part

        # print your encrypted string
        print(estring)

        # if you have the clipboard module installed add it to the clipboard, make it so that you can paste it wherever you prefer
        if paperclip == True:
            pyperclip.copy(estring)
            print('Your encrypted phrase is in your paperclip')

    # Main Decryption program
    def decrypt(self):
        # assign user input to local variable
        usr = self.usrinput

        # Separate the first key and text
        key = int(ord(usr[:usr.index(":")])-ord('a'))
        text = usr[usr.index(":")+1:]
        
        # create final product number one
        part = ""

        # for character in the text reconvert the text back with the converted cipher in to a number
        for ch in text:
            if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
                newCode = ord(ch) - key
                if (newCode < ord('a')):
                    newCode += 26
                part += chr(newCode)
            elif ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
                newCode = ord(ch) - key
                if (newCode < ord('A')):
                    newCode += 26
                part += chr(newCode)
            else:
                part += ch

        # reassign final product to a different variable
        usrinput = part

        # reverse the letter order
        usrinput = usrinput[::-1]

        # Separate the second key and text
        key = usrinput[:usrinput.index("^")]
        usrinput = usrinput[usrinput.index("^")+1:]

        # Create the counter-dictionary to reverse back to the common letters
        decrypt = {
            key[0]: "e",
            key[1]: "a",
            key[2]: "r",
            key[3]: "i",
            key[4]: "o",
            key[5]: "t"
        }

        # create final second product and a counter that will keep track of how far into the string it is
        perfect = ""
        count = 0

        # For character in encrypted phrase, if it matches the according key, then change back to the common letter
        for input in usrinput:
            # Start an exception handling phrase
            try:

                # check for marker of a changed letter marker
                if str(usrinput[count+1]) == "$":
                    perfect += decrypt[input]
                elif input == "$":
                    count += 1
                    continue
                else:
                    perfect += input
                count += 1
            
            # When the phrase errors, finish the statement
            except:
                perfect += input
        
        # make sure that the last 
        if perfect[len(perfect)-1] == "$":
            perfect = perfect[:len(perfect)-1]

        # print the decrypted phrase
        print(perfect)



def main():
    options = False

    # Start a while loop to prevent invalid inputs
    while options == False:
        # grab both user inputs
        choice = input('Encrypt, Decrypt, Info or Exit to end the program  : ').lower()       

        # Create options that people could enter to trigger commands
        echoices = ['e', 'encrypt', 'encode']
        dchoices = ['d', 'decrypt', 'decode']
        ichoices = ['i', 'info', 'facts', 'information']
        xchoices = ['x', 'exit', 'stop', 'end']

        # Check if input is in choices
        # If it is then run the commands in the class to encrypt/decrypt
        if choice in echoices:
            
            personinput = input('Enter the message: ')

            # Creates a  default message if the field is empty
            if len(personinput) == 0:
                personinput = "hello world"

            # instanciate the class
            myinst = cypher(personinput)

            # Check for symbols that could mess up the encryption
            if "^" in personinput or ":" in personinput:
                print('Invalid Inputs, no " ^ " or " : "')
                time.sleep(1)
                continue
            else:
                myinst.encrypt()

        # decrypt the user input
        elif choice in dchoices:
            personinput = input('Enter the message: ')

            # Creates a  default message if the field is empty
            if len(personinput) == 0:
                print('Please enter a valid message\n\n')
                time.sleep(1)
                continue

            # instanciate the class
            myinst1 = cypher(personinput)
            myinst1.decrypt()

        elif choice in ichoices:
            info.info()

        elif choice in xchoices:
            exit = input('Are you sure you want to exit (y/n): ').lower()
            if exit == 'y':
                options = True
            else:
                continue

        # if input is invalid alert user and redo
        else:
            print('invalid input')
            time.sleep(2)

    print('Thank you for using the Couture Cypher')
    input('Press enter to continue')

if __name__ == '__main__':
    main()
    