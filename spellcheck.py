# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import time 
import random 

def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    
    
    menuloop = True
    while menuloop:
        print("")
        print("1. Spell Check A Word (Linear)")
        print("2. Spell check a Word (Binaray)")
        print("3.Spell Check Alice in Wonderland (Linear Search)")
        print("4. Spell Check Alice in Wondeland (Binary Serach)")
        print("5. Exit")
        slc = (input("Selection from 1-5\n"))
        
        if slc == "1":
            
            userinput = input("Type out a word\n")
            userinput = userinput.lower()
            startTimer = time.time()
            check = linearSearch(dictionary, userinput)
            endtimer = time.time()
            if check == -1:
                print(userinput + " Was not found\n")
                print(f"Time Elaseped:" + str((endtimer - startTimer)))
            else: 
                print(userinput + " Was found at" + str((check)))
                print( "Time Elasped: " + str((endtimer - startTimer)) + "seconds")
        elif slc == "2":
            userinput = input("Type out a word\n")
            userinput = userinput.lower()
            startTimer = time.time()
            check = binarySearch( dictionary, userinput)
            endtimer = time.time()
            if check == -1:
                print(userinput + " Was not found")
                print("Time Elaseped:" + str((endtimer - startTimer)))
            else: 
                print(userinput + " Was found at" + str((check)))
                print( "Time Elasped: " + str((endtimer - startTimer)) + "seconds")
        elif slc == "3":
            counter = 0
            timeStart = time.time()
            for i in range(len(aliceWords)):
                check = linearSearch(dictionary, aliceWords[i])
                if check == -1:
                    counter += 1
            timeEnd = time.time()
            print(f" Total words not found {counter}")
            print(f"Total time: {(timeEnd - timeStart)} seconds")
        elif slc == "4":
            counter = 0
            timeStart = time.time()
            for i in range(len(aliceWords)):
                check = binarySearch(dictionary, aliceWords[i])
                if check == -1:
                    counter += 1
            timeEnd = time.time()
            print(f" Total words not found {counter}")
            print(f"Total time: {(timeEnd - timeStart)} seconds")
        elif slc == "5":
            print("Bye Joe")
            menuloop = False
        

        
           
            
            
            
            
# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()

def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
 
    return -1


def binarySearch(anArray, item):
   
  lowerIndex = 0
  upperIndex = len(anArray) - 1
 
  while lowerIndex <= upperIndex:
    middleIndex = (lowerIndex + upperIndex) // 2
   
    if item == anArray[middleIndex]:
      return middleIndex
 
    elif item < anArray[middleIndex]:
      upperIndex = middleIndex - 1
     
    else:
      lowerIndex = middleIndex + 1
  return -1


# Call main() to begin program
main()