#!/usr/bin/env python
# knot-another-gauge-calculator (KAGC [not to be confused with the Allegheny County Airport, PA])
# a knitting gauge calculator, written in python

import time

fine = 'nope' # maybe nice cup of tea will help?

print('To approximate the desired gauge, knit a square swatch the same stich pattern as used in the project.\n')
print('For accurate measurement, the swatch should be a square of at least 4 inches, but larger is preffered.\n')
print('When complete, the number of rows should be the same as the number of stitches.\n')
time.sleep(2)

while fine == 'nope' :
    width   = input('What is the width of your swatch, in inches? \n(measure the top or bottom) ')
    length  = input('\nWhat is the length of your swatch, in inches? \n(measure the sides) ')
    stitches = input('\nHow many stitches per row did you knit? ')
    rows    = input('\nHow many rows did you knit? ')
    fine = 'yep'

    swatch_strings = [width, length, stitches, rows]
    swatch  = []

    try:
        for item in swatch_strings :
            swatch.append(float(item))
    except:
        time.sleep(1)
        print('\nHmm, something\'s not right, want to try that again, with just numbers?\n')
        fine = 'nope'

# stitch gauge = stitches / width
stitch_gauge = swatch[2] / swatch[0]

# row gauge = rows / length
row_gauge = swatch[3] / swatch[1]

print('\nYour row gauge is {} and your stich gauge is {}'.format(round(row_gauge, 2), round(stitch_gauge, 2)))

# checking how square it is

squareness = abs(row_gauge / stitch_gauge)

if 1.2 >= squareness >= 0.8 :
    msg = 'pretty square'
elif 1.5 >= squareness >= 0.5 :
    msg = 'respectably square'
else :
    msg = 'not square at all'

print('\nYour width-to-length ratio is {}, that\'s {}.'.format(round(squareness, 3), msg ))

print('\nHave a nice rest of your day!')
