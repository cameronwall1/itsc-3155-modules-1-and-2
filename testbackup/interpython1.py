
def uniqueElements () :
    x = 0
    my_list = []
    unique_list = []
    print ("Enter seven integers")
    while (x < 7) :
        my_list.append(input(str(x + 1) + ". "))
        x+=1

    for i in my_list :
        if (unique_list.__contains__(i)) :
            print ("", end = "")
        else :
            unique_list.append(i)

    print (my_list)
    print (unique_list)

# uniqueElements()

def getCombinedDict (): 
    my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
    my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}

    d = {}
    for i in range (5) :
        keys = input("Enter one letter from the alphabet: ")
        value = int(input("Enter one integer value: "))
        d[keys] = value

    c = {}
    for i in range (5) :
        keys = input("Enter one letter from the alphabet: ")
        value = int(input("Enter one integer value: "))
        c[keys] = value


    finaldict = {}
    index1 = []
    finalindex = []
    index2 = []
    templist = []
    temp = 0
    y = 0

    for i in d :
        if (i in c) :
            convert =  (str([list(d.keys()).index(i)]))
            convert = convert.strip("[]")
            index1.append(convert)

            convert = (str([list(c.keys()).index(i)]))
            convert = convert.strip("[]")
            index2.append(convert)

    index1 = [int(x) for x in index1]
    index2 = [int(x) for x in index2]

    while (y < len(index1)):
         temp = ((int(str(list (d.values())[index1[y]]))) + int(str(list (c.values())[index2[y]])))
         templist.append(temp)
         y+=1    

    for s in index1:
        finalindex.append((str(list (d)[s])))
    
    l = 0
    while (l < len(templist)):
        finaldict[finalindex[l]] = templist[l]
        l+=1
    print (finaldict)

# getCombinedDict ()

def letterCount (countletters) :
    initialList = list(countletters)
    adjustedlist1 = []
    dict = {}
    y = 0

    for i in initialList :
        if (i not in adjustedlist1) :
            adjustedlist1.append(i)
        else :
            print ("", end = "")
    
    keys = adjustedlist1

    for x in keys:
        dict[x] = 0
    
    while (y < len(keys)) :
        for b in initialList :
            if ((str(list (dict.keys())[y])) == b) :
                currentval = (int(str(list (dict.values())[y])))
                currentval = currentval+1
                dict [b] = currentval
        y+=1
    print (dict)

# letterCount("hello world")

def addfiveintegers () :
    addedIntegers = []
    i = 1
    currentBool = True
    total = 0
    while (len(addedIntegers) < 5) :
        x = (input ("Enter int #" + str(i) + ": "))
        if (x.isdigit()) :
            addedIntegers.append (x)
            i+=1
            currentBool = True

        else :
            currentBool = False
            while (currentBool is not True) :
                x = input ("Please enter an integer: ")
                if (x.isdigit()):
                    print ("Value is an integer")
                    addedIntegers.append(x)
                    i+=1
                    currentBool = True
    
    print (addedIntegers)
    addedIntegers = [int(x) for x in addedIntegers]
    for i in addedIntegers :
        total += i
    print ("Total: " + str(total))
# addfiveintegers ()

# _________________________________________________________________________
# This one works a bit better.. less code too
def addIntegersTwo () :

    addedIntegers1 = []
    i = 1
    total = 0
    while (len(addedIntegers1) < 5) :
        x = input ("Enter int #" + str(i) + ": ")
        if (x.isdigit()) :
            addedIntegers1.append(x)
            i+=1
        else :
            while (x.isdigit() == False) :
                x = input ("Please enter an integer: ")
                if (x.isdigit()):
                 addedIntegers1.append(x)
                 i+=1

    addedIntegers1 = [int(x) for x in addedIntegers1]
    for i in addedIntegers1 :
        total += i
    print ("Total: " + str(total))

# addIntegersTwo()

        
