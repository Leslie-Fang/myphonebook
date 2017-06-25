
def choice1():
   # print("choice 1")
    choosedName = raw_input("Please enter the person's name:").strip().upper()
    if phonebook.get(choosedName) is None:
        print(choosedName+" not found")
    else:
        print(choosedName+" "+phonebook[choosedName])
    outputDic()

def choice2():
    #print("choice 2")
    inputName = raw_input("Please enter the new person's name:").strip().upper()
    print("Please enter the phone number for ts eliot in this format: xxx.xxx.xxxx")
    inputNumber = raw_input().strip().upper()
    phonebook[inputName]=inputNumber
    outputDic()

def choice3():
    #print("choice 3")
    inputName = raw_input("Please enter the person to remove:").strip().upper()
    if phonebook.get(inputName) is None:
        print(inputName+" not found")
        outputDic()
        return
    phonebook.pop(inputName)
    outputDic()

def choice4():
    print("choice 4")

def choice5():
    print("choice 5")

def outputDic():
    print('''*********************************************
Thank you for using the phonebook. Here are your contacts:''')
    for item in phonebook:
        print(item+" "+phonebook[item])
    print("  ")


if __name__ == "__main__":
    phonebook = {'BOB WIN':'021.888.8881','ALEX':'021.888.8882','LUNA HH':'021.888.8883',
                 'JAMES GJ':'021.888.8884','KING':'021.888.8885','HENRY':'021.888.8886'}
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
        choosedItem = raw_input ("Please make a selection:").strip()
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


