# lab02.py, CS 8
# Romina Sarfehnia

def getNumChars(listOfElements):
    ''' Function that takes in a list of elements, and returns
    the number of characters for all strings in listOfElements.
    * listOfElements can contain values of any type.
        * Note you can check if an element is a string with
        type(value) == str
    * If no elements in listOfElements are strings, return 0.
        * Note that an empty string ('') is considered to have
        0 characters.
    '''
    characters = 0
    for element in listOfElements:
        if type(element) == str:
            for i in range(len(element)):
                characters += 1
                
    if characters == 0:
        return 0
    return characters

assert getNumChars([]) == 0
assert getNumChars([1, 2.4, True]) == 0
assert getNumChars(["", None]) == 0
assert getNumChars(["", "\n", " "]) == 2
assert getNumChars(["Python", "is", "awesome"]) == 15
assert getNumChars(["one", 2, "three", 4.0]) == 8
assert getNumChars(["one", "two", 3, "four", "five"]) == 14

def countMultiples(listOfElements, x):
    ''' Function that takes in a list of elements and an integer > 0 (x),
    and returns the number of items in listOfElements that are
    multiples of x.
    * listOfElements can contain values of any type.
    * If no elements exist in listOfElements, return 0.
    * If no numerical elements exist in listOfElements, return 0.
    '''
    count = 0
    for element in listOfElements:
        if type(element) == int or type(element) == float:
            if element % x == 0:
                count += 1

    return count

assert countMultiples([], 1) == 0
assert countMultiples([4, 8, 12, 16, 20], 4) == 5
assert countMultiples([-2, 3, 4, -5, 6.1, 9], 3) == 2
assert countMultiples(["one", 2, "three", 4.0], 2) == 2
assert countMultiples(["Python", "is", "awesome"], 5) == 0

def getLongestString(listOfElements):
    ''' Function that takes in a list of elements, and returns
    the string with the most number of characters.
    * listOfElements can contain values of any type.
    * If no elements in listOfElements are strings, return
    None.
    * If two or more largest strings have the same number of
    characters, return the first string in the order it
    appears in listOfElements (lower index).
    '''
    max_length = ""
    no_strings = False
    no_strings_count = 0
    
    for element in listOfElements:
        if type(element) == str:
            if len(element) > len(max_length):
                max_length = element
        else:
            no_strings_count += 1

    if no_strings_count == len(listOfElements):
        return None

    return max_length

assert getLongestString([]) == None
assert getLongestString([1, 2.4, True]) == None
assert getLongestString(["", None]) == ""
assert getLongestString(["Abcd", "abc", "bc"]) == "Abcd"
assert getLongestString(["Python", "is", "awesome"]) == "awesome"
assert getLongestString(["one", 2, "three", 4.0]) == "three"
assert getLongestString(["one", "two", "four", "five"]) == "four"
assert getLongestString(["one", "two", 3, "four", "five"]) == "four"

def removeMultiples(listOfElements, x):
    ''' Function that takes in a list of elements and an integer > 0 (x),
    and returns a new list containing all elements in listOfElements
    EXCEPT the items that are multiples of x.
    * listOfElements can contain values of any type.
    * Elements in the returned list must occur in the order they
    appear in listOfElements
    * Hint, think of the accumulator pattern, but instead of counting
    we're accumulating a collection
    '''
    multiples = []

    for element in listOfElements:
        if type(element) == int or type(element) == float:
            if element % x != 0:
                multiples.append(element)
        else:
            multiples.append(element)

    return multiples

assert removeMultiples([], 1) == []
assert removeMultiples([4, 8, 12, 16, 20], 4) == []
assert removeMultiples([-2, 3, 4, -5, 6.1, 9], 3) == [-2, 4, -5, 6.1]
assert removeMultiples(["one", 2, "three", 4.0], 2) == ["one", "three"]
assert removeMultiples(["Python", "is", "awesome"], 5) == ["Python", "is", "awesome"]

def organizeWords(listOfStr):
    ''' Function that takes in a list of strings, and returns a dictionary
    where the keys are capital characters, and each key's corresponding
    value is a list containing all strings in listOfStr (in all capital
    letters) that start with the key character in capital letters in the order that they appear in listOfStr.
    * An empty listOfStr should return an empty dictionary
    * You may assume listOfStr ONLY contains string elements (or is empty)
    * The empty string ('') should not be stored in the dictionary
    * Consider using the string's .upper() method when creating keys in
    the dictionary, and creating list values in the dictionary.
    '''
    new_dict = {}
    for element in listOfStr:
        if type(element) == str:
            if element != "":
                if element[0].upper() in new_dict:
                    new_dict[element[0].upper()].append(element.upper())
                else:
                    new_dict[element[0].upper()] = [element.upper()]

    return new_dict

assert organizeWords([]) == {}

D = organizeWords(["CS8"])
assert ("C" in D) == True
assert ("c" in D) == False
assert D["C"] == ["CS8"]

D = organizeWords(["Python", "is", "awesome", ""])
assert ("i" in D) == False
assert ("P" in D) == True
assert ("I" in D) == True
assert ("A" in D) == True
assert ("a" in D) == False
assert ("" in D) == False
assert D["P"] == ["PYTHON"]
assert D["I"] == ["IS"]
assert D["A"] == ["AWESOME"]

D = organizeWords(["Ant", "antler", "ART", "Car", "", "bee", "can"])
assert ("b" in D) == False
assert ("B" in D) == True
assert ("a" in D) == False
assert ("A" in D) == True
assert ("C" in D) == True
assert ("" in D) == False
assert D["A"] == ["ANT", "ANTLER", "ART"]
assert D["C"] == ["CAR", "CAN"]
assert D["B"] == ["BEE"]        
