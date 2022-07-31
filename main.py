from random import choice
import argparse
import sys

EYES=[':',';','=','X','8','B']
MOUTHS=['|',')','(','C','O','P','p','b','^','3','w','D','d','I','v','>','<','X',']','[','}']

def random_emoticon(n=1):
    '''prints n random emoticon'''
    for i in range(n):
        eye=choice(EYES)
        while True:
            mouth=choice(MOUTHS)
            if mouth!=eye: # checks eyes and mouth are not the same character cuz that'll be kinda ugly
                break
        sys.stdout.write(f'{eye}{mouth}\n')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', type=int, default=1,
                        help='number of random emoticons?')
    args = parser.parse_args()
    random_emoticon(n=args.n)

if __name__=='__main__':
    main()
