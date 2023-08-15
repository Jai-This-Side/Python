weight = int(input('enter your weight\n'))
choice = int(input('press 1 for converting kilogram to pound\npress 2 for converting pound to kilogram\n'))

if(choice == 1):

    kilogram = int(input('enter your weight in kilogram\n'))
    pound = int(kilogram)*2.20462
    print('your weight in pound is ' + str(pound))

if(choice == 2):

    pounds = input('What is your weight (lbs)\n')
    kilogram = int(pounds) * 0.45
    print('your weight in kilogram is ' + str(kilogram))