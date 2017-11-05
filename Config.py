import random
# 0 - infantry
# 1 - cavalry
# 2 - police
# 3 - gun
# 4 - signalman
# 5 - bomberman
# 6 - tank
spawn_k = 0.3
types = ['infantry','cavalry','police','gun','signalman','bomberman','tank']
fractions = ['bolshevik','white','german_empire','britain','russian_empire']
health = [3,3,2,2,2,2,5]
damage = [
    [2,1,1,1,1,1,1], # infantry
    [1,1,2,1,2,2,1], # cavalry
    [1,1,1,1,2,2,1], # police
    [3,6,1,1,1,1,1], # gun
    [1,1,1,1,1,1,1], # signalman
    [1,1,1,1,1,1,2], # bomberman
    [6,5,1,6,1,1,3]  # tank
]

def skill(id, lose_a, lose_b, fraction):
    if fraction=='bolshevik':
        if types[id]=='signalman':
            if random.randint(0,100)>80:
                print('BOLSHEVIK: ENEMY IS NEAR!')
                lose_a = [x-1 for x in lose_a]
        elif types[id]=='bomberman':
            if random.randint(0,100)>90:
                print('BOLSHEVIK: DESTROY OLD ORDER!')
                lose_b[types.index('gun')] += 5
    elif fraction=='white':
        if types[id]=='infantry':
            if random.randint(0,100)>50:
                print('WHITE: OFFICIERS OF IMPERIAL ARMY!')
                lose_a = [x-1 for x in lose_a]
                lose_b = [x+1 for x in lose_b]

    if types[id]=='signalman':
        if random.randint(0,100)<90:
            print('ТРЕВОГА!')
            lose_a = [x-1 for x in lose_a]

    return lose_a, lose_b
