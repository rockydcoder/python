import logging
class Person:
    def __init__(self, name, number):
        self.name = name
        self.number = number

def binarySearchByName(aList, name):
    if len(aList) == 1:
        if aList[0].name == name:
            print aList[0].name + " " + aList[0].number
        return
    else:
        mid = len(aList)//2
        if aList[mid].name == name:
            print aList[mid].name + " " + aList[mid].number
            return
        elif name < aList[mid].name:
            binarySearchByName(aList[:mid], name)
        elif name > aList[mid].name:
            binarySearchByName(aList[mid:], name)

def binarySearchByNumber(aList, number):
    if len(aList) == 1:
        if aList[0].number == number:
            print aList[0].name + " " + aList[0].number
        return
    else:
        mid = len(aList)//2
        if aList[mid].number == number:
            print aList[mid].name + " " + aList[mid].number
            return
        elif number < aList[mid].number:
            binarySearchByNumber(aList[:mid], number)
        else:
            binarySearchByNumber(aList[mid:], number)


f = open('contacts.txt', 'r')
persons = []
for line in f:
    array = line.split("|")
    newPerson = Person(array[0], array[1].strip())
    persons.append(newPerson)
f.close()
while True:
    var = raw_input("L)ookup Name, Lookup N)umber or Q)uit? ")
    if var == 'L':
        persons.sort(key=lambda person: person.name)
        name = raw_input("Enter the name: ")
        binarySearchByName(persons, name)

    elif var == 'N':
            persons.sort(key=lambda person: person.number)
            number = raw_input("Enter the number: ")
            binarySearchByNumber(persons, number)
    else:
        if var == 'Q':
            break




