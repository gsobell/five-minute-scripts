#!/usr/bin/env python
# no, I did not know any python when I wrote this

leave = 'n'

todo = []

#load = open('updated_list.txt','r')
#todo = load.read()
while leave != 'y' :
    
    view = input("Would you like to see some of the things we're going to do this week? [y/n]")
    
    if view == 'y':
        for task in todo :  
            print(task)
    add = input("Would you like to add somthing to the list? [y/n]")
    
    if add == 'y':
        newitem = input("What else would you like to do? " )
        todo.append(newitem)
    print(task)
    leave = input("Would you like to exit? [y/n]")

    if leave == 'y' :
        print("'Your updated list will be found in the same directory as this program was run! It's called 'updated list'")
    print(todo, file=open('updated_list.txt','w'))
