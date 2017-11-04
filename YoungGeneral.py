# 0 - infantry
# 1 - cavalry
# 2 - police
# 3 - gun
# 4 - signalman
# 5 - bomberman

import random
import sys
import os
random.seed()

spawn_k = 70
types = ['infantry','cavalry','police','gun','signalman','bomberman']
health = [2,2,1,1,1,1]
damage = [
    [2,1,1,1,1,1], # infantry
    [1,1,2,1,2,2], # cavalry
    [1,1,1,1,2,2], # police
    [3,6,1,1,1,1], # gun
    [0,0,0,0,0,0], # signalman
    [0,0,0,0,0,0]  # bomberman
]

def skill(id, lose_a, lose_b, fraction):
    if fraction==0:
        if types[id]=='signalman':
            if random.randint(0,100)>80:
                print('BOLSHEVIK: ENEMY IS NEAR!')
                lose_a = [x-1 for x in lose_a]
        elif types[id]=='bomberman':
            if random.randint(0,100)>90:
                print('BOLSHEVIK: DESTROY OLD ORDER!')
                lose_b[types.index('gun')] += 5
    else:
        if types[id]=='infantry':
            if random.randint(0,100)>50:
                print('WHITE: OFFICIERS OF IMPERIAL ARMY!')
                lose_a = [x-1 for x in lose_a]
                lose_b = [x+1 for x in lose_b]
    return lose_a, lose_b

def fight(a, b):
    # fight
    f_a = [0]*len(types)
    for i in range(len(a)):
        for j in range(len(types)):
            f_a[j] += random.randint(0,damage[a[i]][j])
    f_b = [0]*len(types)
    for i in range(len(b)):
        for j in range(len(types)):
            f_b[j] += random.randint(0,damage[b[i]][j])

    # loses count
    lose_a = [0]*len(types)
    lose_b = [0]*len(types)
    for i in range(len(types)):
        lose_a[i] = f_b[i]//health[i]
        lose_b[i] = f_a[i]//health[i]

    # skills
    for i in range(len(a)):
        lose_a, lose_b = skill(a[i],lose_a,lose_b,0)
    for i in range(len(b)):
        lose_b, lose_a = skill(b[i],lose_b,lose_a,1)
    for i in range(len(types)):
        lose_a[i] = max(0,min(lose_a[i],a.count(i)))
        lose_b[i] = max(0,min(lose_b[i],b.count(i)))

    return lose_a, lose_b

while True:
    event = input()

    if event=='fight':
        red = []
        print('Red forces:')
        for i in range(len(types)):
            q = int(input(types[i]+': '))
            red += [i]*q
        white = []
        print('White forces: ')
        for i in range(len(types)):
            q = int(input(types[i]+': '))
            white += [i]*q
        res = fight(red, white)
        print('Red loses:')
        for i in range(len(types)):
            print(types[i]+' '+str(res[0][i]),end=' ')
        print()
        print('White loses:')
        for i in range(len(types)):
            print(types[i]+' '+str(res[1][i]),end=' ')
        print()
    elif event=='spawn':
        p = random.randint(1,100)
        if p>spawn_k:
            print('New soldier!')
        else:
            print('No reserve!')
    elif event=='clear':
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print('Strange event...')
