from pokemon import Pkmn

points = 0

#Test 1
try:
    trainer1 = Pkmn('Blue',{},0,6,['Boulder','Cascade','Thunder'])
    trainer2 = Pkmn('Red',{},0,6,['Boulder'])

    badges = Pkmn.whichMedals(trainer1,trainer2)

    assert badges == ['Cascade','Thunder']
    points += 3
except:
    print("Test 1 failed")
    points += 0

#Test 2
try:
    trainer1 = Pkmn('Blue',{},0,6,['Boulder'])
    trainer2 = Pkmn('Red',{},0,6,['Cascade','Thunder'])

    badges = Pkmn.whichMedals(trainer1,trainer2)

    assert badges == ['Boulder']
    points += 3
except:
    print("Test 2 failed")
    points += 0



print("You got: " + str(points) + "/6 points")