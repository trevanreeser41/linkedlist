from linkedlist_api import LinkedList
import csv

linkedList = LinkedList()

linkedList.add(1)
linkedList.add(2)
linkedList.add(3)
linkedList.debug_print()
linkedList.set(1,0)
a=linkedList.get(1)
linkedList.debug_print()
linkedList.swap(0,1)
print(a)
linkedList.debug_print()
linkedList.insert(1,9)
linkedList.debug_print()
linkedList.delete(0)
linkedList.debug_print()

with open('data_example.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        items = row[0].split(",",1)
        parameters=items[1].split(",")
        action = items[0]
        if action ==  'CREATE':
            linkedList = LinkedList()
        elif action == 'DEBUG':
            linkedList.debug_print()
        elif action == 'ADD':
            print(action,parameters)
            linkedList.add(parameters[0])
        elif action == 'SET':
            print(action,parameters)
            linkedList.set(int(parameters[0]),parameters[1])
        elif action == 'GET':
            print(action,parameters)
            linkedList.get(int(parameters[0]))
        elif action == 'DELETE' :
            print(action,parameters)
            linkedList.delete(int(parameters[0]))
        elif action == 'INSERT':
            print(action,parameters)
            linkedList.insert(int(parameters[0]),parameters[1])
        elif action == 'SWAP':
            print(action,parameters)
            linkedList.swap(int(parameters[0]),int(parameters[1]))
        else:
            print("Blow up!")