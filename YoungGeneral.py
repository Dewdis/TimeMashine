import random
import sys
import os
random.seed()

from Config import *

def fight(a, b, fraction_a, fraction_b):
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

        if lose_a[i]==0 and random.uniform(0,1)<f_b[i]/health[i]:
            lose_a[i]=1
        if lose_b[i]==0 and random.uniform(0,1)<f_a[i]/health[i]:
            lose_b[i]=1

    # skills
    for i in range(len(a)):
        lose_a, lose_b = skill(a[i],lose_a,lose_b,fraction_a)
    for i in range(len(b)):
        lose_b, lose_a = skill(b[i],lose_b,lose_a,fraction_b)
    for i in range(len(types)):
        lose_a[i] = max(0,min(lose_a[i],a.count(i)))
        lose_b[i] = max(0,min(lose_b[i],b.count(i)))

    return lose_a, lose_b

while True:
    event = input()

    if event=='fight':
        forces_1 = []
        print('forces 1:')
        fraction_1 = input('fraction: ')
        if not(fraction_1 in fractions):
            print('Unknown fraction!')
            continue
        for i in range(len(types)):
            q = int(input(types[i]+': '))
            forces_1 += [i]*q
        forces_2 = []
        print('forces 2: ')
        fraction_2 = input('fraction: ')
        if not(fraction_2 in fractions):
            print('Unknown fraction!')
            continue
        for i in range(len(types)):
            q = int(input(types[i]+': '))
            forces_2 += [i]*q
        res = fight(forces_1, forces_2, fraction_1, fraction_2)
        print(fraction_1+' loses:')
        for i in range(len(types)):
            print(types[i]+' '+str(res[0][i]),end=' ')
        print()
        print(fraction_2+' loses:')
        for i in range(len(types)):
            print(types[i]+' '+str(res[1][i]),end=' ')
        print()
    elif event=='spawn':
        p = random.uniform(0,1)
        if p<spawn_k:
            print('New soldier!')
        else:
            print('No reserve!')
    elif event=='clear':
        os.system('cls' if os.name == 'nt' else 'clear')
    elif event=='health':
        print(health)
    elif event=='damage':
        for i in range(len(damage)):
            print(damage[i])
    elif event=='types':
        print(types)
    elif event=='fractions':
        print(fractions)
    else:
        print('Strange event...')
