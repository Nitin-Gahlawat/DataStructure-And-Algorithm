from String.Anagram import Anagram
from String.Duplicates import Duplicates
from String.Plindrome import Plindrome
from String.Reverse import Reverse
from String.WorkingWithCase import Working_with_case
from String.BasicOpration import BasicOprations
from String.Permutataion import Purmutation
from String.Anagram import Anagram



# ## Basics of conversion of character to Ascii or Vice versa
## Basic intoduction to Charaters/String in python
def introduction():
    print("\nString")
    print("-"*120)
    print("This Module contains all the algorithm related to the String datastructure")
    print("Basic of String ")
    #printing the ascii(0-127) 7 bits value of the charater 
    #unicode(takes 16bytes) displayed in form of the hex decimal (eg C03A)
    print("Conversion form String type to ascii using ord function")
    print(f"H {ord('H')}")
    print(f"I ord('I')")
    print(f"0 ord('0')")
    print(f"9 ord('9')")
    #print charater of the ascii value given
    print("Conversion of ascii values to String using chr function")
    print("72 "+chr(72))
    print("73 "+chr(73))

