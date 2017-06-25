
def choice1():
    print("choice 1")

def choice2():
    print("choice 2")

def choice3():
    print("choice 3")

def choice4():
    print("choice 4")

def choice5():
    print("choice 5")

if __name__ == "__main__":
    phonebook = {'BOB':'021888881','ALEX':'021888882','LUNA':'021888883',
                 'JAMES':'021888884','KING':'021888885','HENRY':'021888886'}
    #for item in phonebook:
    #    print item
    #    print phonebook[item]

    print ("Welcome to the Python Phonebook")
    print ('''Main Menu
1. Find a number
2. Add a person
3. Remove a person
4. Change a person's number
5. Reverse lookup''')
    while 1:
        choosedItem = input ("Please make a selection:").strip()
        print ("choosedItem is "+choosedItem)
        if choosedItem == "1":
            choice1()
        elif choosedItem == "2":
            choice2()
        elif choosedItem == "3":
            choice3()
        elif choosedItem == "4":
            choice4()
        elif choosedItem == "5":
            choice5()


