#!/usr/bin/env python

# caffeine contents are aprox, will vary with strength of brewing/infusion
# per standard serving, rather than volume
# given in mg

drinks = [drip_coffee : 00,black_tea : 45,green_tea : 30,matcha : 00,espresso : 75,can_cola : 35,bottle_cola : 00,energy_drink : 300,]

valid_unit = 'no'
drink = input('What did you drink?')


while valid_unit == 'no': 
    weight = input('Please input weight, followed by kg or lb: ')
    if weight[-2] == 'l' :
        print('hi')
        valid_unit = 'imperial, but I guess it\'s ok.'
    elif weight[-2] == 'k' :
        print('hi there')
        valid_unit = 'metric'
    else :
        valid_unit = 'no'


# A lethal dose of caffeine (LD50) consumed orally is equivalent to about 150 milligrams per kilogram of body weight

150mg_dose = 150/drink


print('You would need to drink ' + (weight * 150mg_dose) + drink_name + ' to kill you.'  )
