print ('enter your name:')
name=input()
print('FBI OPEN UP!!!\n1 to open. 2 to run to the secret exit')
anwsA=input()
if anwsA==('1'):
    print ('FBI killed you.\n This is end')
elif anwsA==('2'):
    print ('You ran to the secret door, but then you open it you see police everythere.\n 1 to run back 2 to quietly go to the roof by the ladder')
    anwsB=input()
    if anwsB==('1'):
        print ('FBI broked your door and killed you.\n You die...')
    elif anwsB==('2'):
        print('You are on the roof.\n1 to call friend 2 to hide somethere')
        anwsC=input()
        if anwsC==('1'):
            print('Sniper killed you.')
        elif anwsC==('2'):
            print ('There to hide?\n1 to run back to the house. 2 to hide in the chimney. 3 to hide in some mini electricity house.')
            anwsD=input()
            if anwsD==('1'):
                 print('FBI broked your door and killed you.\n You die...')
            elif anwsD==('2'):
                print ('you fell down thou the chimney')
            elif anwsD==('3'):
                print('You ran to the house.\nYou are calling your friend...\nCALL: BEEB, BEEB, BEEB, BEEB,FRIEND: Hi ',(name),'that?\nYOU:I need help, some police or FBI or bouth want to kill me!\nFRIEND:It is not funny, sorry I do not have time for jokes! BEEB, BEEB, BEEB,BEEB...')
                print ('1 to cut each cabel to put off electicity in all house 2 to run back to the roof.')
                anwsE=input()
                if anwsE==('2'):
                    print('Sniper killed you.')
                elif anwsE==('1'):
                    print ('There is no electicity in your street')
