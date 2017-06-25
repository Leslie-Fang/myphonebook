
def choice1():
    choosedName = input("Please enter the person's name:").strip().upper()
    if phonebook.get(choosedName) is None:
        print(choosedName+" not found")
    else:
        print(choosedName+" "+phonebook[choosedName])
    outputDic()

def choice2():
    inputName = input("Please enter the new person's name:").strip().upper()
    print("Please enter the phone number for ts eliot in this format: xxx.xxx.xxxx")
    inputNumber = input().strip().upper()
    phonebook[inputName]=inputNumber
    outputDic()

def choice3():
    inputName = input("Please enter the person to remove:").strip().upper()
    if phonebook.get(inputName) is None:
        print(inputName+" not found")
        outputDic()
        return
    phonebook.pop(inputName)
    outputDic()

def choice4():
    inputName = input("Please enter the person whose number you wish to change:").strip().upper()
    if phonebook.get(inputName) is None:
        print(inputName+" not found")
        outputDic()
        return
    else:
        print("The number for "+inputName+" is currently "+phonebook[inputName])
    print("Please enter the new number for ernest hemingway in this format: xxx.xxx.xxxx")
    inputNumber = input().strip().upper()
    phonebook[inputName]=inputNumber
    outputDic()

def choice5():
    inputNumber = input("Please enter the person's number in this format: xxx.xxx.xxxx   ").strip().upper()
    for item in phonebook:
        if phonebook[item] == inputNumber:
            print(item+" "+phonebook[item])
            outputDic()
            return
    print("This phone number is not in the list")

def outputDic():
    print('''*********************************************
Thank you for using the phonebook. Here are your contacts:''')
    for item in phonebook:
        print(item+" "+phonebook[item])
    print("  ")

if __name__ == "__main__":
    phonebook = {'BOB WIN':'021.888.8881','ALEX':'021.888.8882','LUNA HH':'021.888.8883',
                 'JAMES GJ':'021.888.8884','KING':'021.888.8885','HENRY':'021.888.8886'}
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


