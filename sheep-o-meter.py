#!/usr/bin/env python
# a small program to determine if you indeed have a sheep.

sheep_points = 0 # How sheep-y is it?
yay = []         # positive evidence
neigh = []       # negative evidence

input('Is that a sheep?')

#'In times like these, it can cause great distress if you are unsure if you have a sheep or not.')

sheep_points += int(float(input('On a scale of 1-10, how fluffy is it?' ))/2.75)

neigh.append(input('Is is made of cotton?[y/n] '))

yay.append(input('Does it solicit people for food? [y/n]'))

yay.append(input('Does it eat grass? [y/n] '))

yay.append(input('Would you say it is somewhat gregarious? [y/n]' ))

yay.append(input('Does it \'baaa\'? [y/n]'))

yummy = input('Does it look yummy?[y/n] ')
if yummy[0] == 'y':
    print('Sheep are friends, not food!')

sheep_points += int(yay.count('y'))
sheep_points += int(neigh.count('n'))

if sheep_points >= 8 :
    print('You definitely have a sheep!')
elif sheep_points <=4 : 
    print('You don\'t have a sheep!')
    input('So...')
    input('What do you have??')
else :
    print('You might have a sheep!')
    
print('Your final sheep score is ' + str(sheep_points) + ' sheep points!')
