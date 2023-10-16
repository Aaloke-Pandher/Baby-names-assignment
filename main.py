# BABY NAMES DATA ASSIGNMENT START CODE

import json

def main():
    # Load Baby Data from File
    file = open("baby-names-data.json")
    baby_data = json.load(file)
    file.close() 

    # Main Menu
    loop = True
    while loop:
        selection = getMenuSelection()

        if selection == "1":
            displayAll(baby_data)
        elif selection == "2":
            searchGender(baby_data)
        elif selection == "3":
            searchRank(baby_data)
        elif selection == "4":
            searchStartLetter(baby_data)
        elif selection == "5":
            searchNameLength(baby_data)
        elif selection == "6":
            print("\nGOODBYE!\n")
            loop = False


def getMenuSelection():
    # Print Menu & Return User Selection
    print("\n*** BABY DATA - MAIN MENU ***")
    print("* 1: Display All")
    print("* 2: Search by Gender")
    print("* 3: Search by Rank")
    print("* 4: Search by Starting Letter")
    print("* 5: Search by Name Length")
    print("* 6: Exit")

    return input("* Enter Option #: ")


def displayAll(baby_data):
    # Display All Baby Data
    print("\nDISPLAY ALL") 
    for i in range(len(baby_data)):
        print(baby_data[i].get("name") + " (Rank: " + str(baby_data[i].get("rank")) + ", Gender: " + baby_data[i].get("gender") + ")")


def searchGender(baby_data):
    # Dislay All Baby Names based on Gender
    print("\nSEARCH BY GENDER") 
    babyGender = input("Enter a gender: ")
    for i in range(len(baby_data)):
        if baby_data[i].get("gender") == babyGender:
            print(baby_data[i].get("name") + " (Rank: " + str(baby_data[i].get("rank")) + ", Gender: " + baby_data[i].get("gender") + ")")


def searchRank(baby_data):
    # Display All Baby Names based on Rank
    minRank = input("Enter a minimum rank: ")
    maxRank = input("Enter a maximum rank: ") 
    for i in range(len(baby_data)):
        if baby_data[i].get("rank") >= int(minRank) and baby_data[i].get("rank") <= int(maxRank):
            print(baby_data[i].get("name") + " (Rank: " + str(baby_data[i].get("rank")) + ", Gender: " + baby_data[i].get("gender") + ")")


def searchStartLetter(baby_data):
    # Insert User Item into a Position
    print("\nSEARCH BY START LETTER") 
    firstLetter = input("Enter first letter: ") 
    for i in range(len(baby_data)): 
        baby_name = baby_data[i].get("name")
        if baby_name[0] == firstLetter: 
            print(baby_data[i].get("name") + " (Rank: " + str(baby_data[i].get("rank")) + ", Gender: " + baby_data[i].get("gender") + ")")


def searchNameLength(baby_data):
    # Remove item from position
    print("\nSEARCH BY NAME LENGTH")
    nameLength = input("Enter name length: ") 
    babycount = 0
    for i in range(len(baby_data)): 
        baby_name = baby_data[i].get("name")
        if len(baby_name)== int(nameLength): 
            print(baby_data[i].get("name") + " (Rank: " + str(baby_data[i].get("rank")) + ", Gender: " + baby_data[i].get("gender") + ")") 
            babycount += 1

# Invoke main to begin program
main()
