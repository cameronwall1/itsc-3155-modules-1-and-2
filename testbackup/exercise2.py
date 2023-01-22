def backwardsString () :
    initialString = input ("Enter a string: ")
    stringList = list(initialString)
    reversedString = ""
    for i in reversed(stringList) :
        reversedString += i
    print (reversedString)

# backwardsString ()

def shiftString () :
    initialString = input ("Enter a string: ")
    uppercaseletters = ""
    lowercaseletters = ""
    stringList = list (initialString)
    for i in initialString :
        if i.isupper() :
            uppercaseletters += i
        elif i == " " :
            print ("", end = "")
        else :
            lowercaseletters += i
    combinedString = lowercaseletters + uppercaseletters
    
    print (combinedString)

shiftString()