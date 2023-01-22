# #Sahiti Moduga, Cameron Wall, Jeffery Xu


x = 123477.7891
i = float(f"{x:.1f}")
print("{:,}".format(i))


x = 123477.7891
print (f"{x:,.1f}")
print(f"{x:<012,.2f}")
print(f"{x:<012,.2f}".format(x))










































# grade = int(input("Enter digit from 0 to 100 "))

# if grade >= 90:
#     print ("A!")
# elif grade < 90 and grade >= 79:
#     print ("B!")
# elif grade < 80 and grade >= 69:
#     print ("C!")
# elif grade < 70 and grade >= 59: 
#     print ("D!") 
# else :
#     print ("F!")

# # _________________________________________________________

# first = input ("Enter one word: ")
# second = input ("Enter another word: ")

# if (second.__contains__(first) or first.__contains__(second)):
#     # print ("match found... the match is " + first)
#     print ("True")
# else :
#     print ("word is not contained within this text")
#     print ("False")

# # _________________________________________________________

# firstInteger = int (input ("Enter a positive integer: "))
# x = 0
# while (x <= firstInteger):
#     print ("The cube of " + str (x) + " is " + str(x * x * x))
#     x += 1

# # _________________________________________________________

# def findAverage ():
#     my_list = []
#     limit = input ("Enter a number: ")
#     for x in range (int(limit)):
#         addInteger = input ("Enter number " + str(x + 1) + ". ")
#         my_list.append(float(addInteger))
#     print (my_list)

#     average = 0
#     for x in my_list:
#         average += x
#     finalAverage = float (average / int(limit))
#     print (finalAverage)
    
# # _________________________________________________________

# findAverage()

# def commonValues () :
#     print ("Please enter 5 integers")
#     firstList = []
#     secondList = []
#     mutualValues = []
#     for x in range (5) :
#         listOneValue = input (" ")
#         firstList.append(listOneValue)

#     print ("Please enter another 5 integers")
#     for x in range (5) :
#         secondOneValue = input (" ")
#         secondList.append(secondOneValue)
    

#     for x in firstList :
#         if (x in secondList) :
#             print ("Value was found " + str(x))
#             mutualValues.append(x)

#     if (not mutualValues) :
#          print ("there are no mutual values between the two lists")
#     else :
#         print (mutualValues)
        

# commonValues()

# # _________________________________________________________

# def grid () :



#     row = int(input("Enter a row number (1-5): "))
#     col = int(input("Enter a column number (1-5): "))

#     for i in range(1, 6):
#         for j in range(1, 6):
#             if i == row and j == col:
#              print(1, end = " ")
#             else:
#               print(0, end = " ")
#         print()
# grid ()

# # _________________________________________________________

# def getEvenNumbers () :
#     my_list = []
#     even_list = []
#     valueone = ""
#     while (valueone.upper() != "QUIT") :
#         print (valueone.upper())
#         valueone = input ("Enter a number or QUIT to quit: ")
#         if (valueone.upper() != "QUIT") :
#             my_list.append(int(valueone))
#     print (my_list)

#     for x in my_list :
#         if ((x % 2) == 0) :
#             even_list.append(x)
#     print (even_list)


# getEvenNumbers()

# # _________________________________________________________


# def appearsOnce () :
#     totalList = []
#     singleValue = []
#     for x in range (10) :
#         value = input ("Enter a number " + str(x + 1) + ": ")
#         if value in totalList :
#             print ("Value was found already")
#             singleValue.remove(value)
#         else :
#             singleValue.append(value)

#         totalList.append(value)

#     print (totalList)
#     print (singleValue)


# appearsOnce()
            
# # _________________________________________________________

# def createString () :
#     words = []
#     for x in range (5) :
#         words.append(input("Enter a word " + (str(x +1) + ": ")))
#     oneString = (words[0] + " " + words[1] + " "  + words[2] + " "  + words[3] + " "  + words[4])
#     print (oneString)

# createString()




# # _________________________________________________________

# def splitString (): 
#     templist = []
#     finallist = []
#     split = input ("Enter a string: ")
#     maxLength = len (split)
#     currentLength = 0
#     beginning = 0
#     end = 3

#     while (end <= maxLength + 1) :
#         print (split[beginning:end])
#         templist.append(split[beginning:end])
#         beginning+=3
#         end+=3
    
#     print ("this is the temp list: ", end ="")
#     print (templist)


#     for x in templist :
#         finallist.append(list(x))
#     print ("this is the final list: ", end ="")
#     print (finallist)

# splitString ()

