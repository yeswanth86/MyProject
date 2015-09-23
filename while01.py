#!/usr/bin/python

number = 7
test = True

while test:
    guess = int(raw_input('Enter an integer:'))

if guess == number:
    print 'you gussed the tight number!!'
    test = False

    elif guess < number:
    print 'The number is a little greater than that'
    else:
    print 'No, the number is litle lower than that'
else:
    print ' The while loop is over.'

print 'Done'
