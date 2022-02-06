from random import choice

EYES=[':',';','=','X','8','B']
MOUTHS=['|',')','(','C','O','P','p','b','^','3','w','D','d','I','v','"','S','>','<','X',']','[','}']

def all():
    '''prints all possible emoticons'''
    for eye in EYES:
        for mouth in MOUTHS:
            if mouth!=eye: # checks eyes and mouth are not the same character cuz that'll be kinda ugly
                print(f'{eye}{mouth}')

def random(n=1):
    '''prints n random emoticon'''
    for i in range(n):
        eye=choice(EYES)
        while True:
            mouth=choice(MOUTHS)
            if mouth!=eye: # checks eyes and mouth are not the same character cuz that'll be kinda ugly
                break
        print(f'{eye}{mouth}')

if __name__=='__main__':
    all()