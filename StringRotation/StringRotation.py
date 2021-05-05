'''
Cracking the coding interview
Chapter 1 - Arrays and Strings page 91
String Rotation
----------------------------------------
Problem Statement: Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check is s2's
rotation of s1 using only one call to isSubstring
example
    input: waterbottle
    output: erbottlewat
Constraits or Questions you need to ask:
-What is a substring
-What is a rotation of a string?
Solution notes:
-First find out how to find if 1 string is a substring of another
-Work on the small solution first
-If both strings are not the same size then it's false
-Make sure both strings are lower cased
'''
import string
string1 = 'vincenzo'
string2 = 'zoncenvi'
string3 = "babel"
string4 = "label"
#print(s1[:]) # returns complete string
 
#print(s1[: 5]) # substring From 0 to 5
 
#print(s1[1 : 10])
 
#print(s1[2 : 13])
 
#print(s1[5 : 15]) # substring from 5 to 15

def bruteForce(s1,s2):
    #First check if both string lengths are the same
    if len(s1) != len(s2):
        return False

    #Make sure both strings are lowercases
    s1 = s1.lower()
    s2 = s2.lower()

    #Sorting both string alphabetically 
    s1 = "".join(sorted(s1))
    s2 = "".join(sorted(s2))

    #If they don't equal then they can't be the same word
    if s1 == s2:
        return True
    else:
        return False

def isSubstring(s1,s2):
    #First check if both string lengths are the same
    if len(s1) != len(s2):
        return False

    #Make sure both strings are lowercases
    s1 = s1.lower()
    s2 = s2.lower()

    #Initalize 2 dictionaries to keep track of letters in both string
    #We're adding the letters from a-z in all lower cases to the dict with values 0
    d1 = dict.fromkeys(list(string.ascii_lowercase),0)
    d2 = dict.fromkeys(list(string.ascii_lowercase),0)

    #Loop through both strings and update their dictionaries on each charcter in that string to have a value of 1
    for i in range(len(s1)):
        d1[s1[i]] += 1
        d2[s2[i]] += 1
    return d1 == d2


#Should be true
#print(isSubstring(string1,string2))

#Should be false
#print(isSubstring(string3,string4))

#Should be true
#print(bruteForce(string1,string2))

#Should be false
#print(bruteForce(string3,string4))



