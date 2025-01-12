import random

NUM_LENGTH:int=3
NUM_CHANCES:int=8
ALLOW_CHARACTERS:bool=False
ALLOW_UPPER_CHARACTERS:bool=False

def main():

##################################################
#######################################################
# presentation:

    print('''Bagels, a deductive logic game
By Al Sweigart with codes improved by Heber-Dsouza

I am thinking of a {}-digit {} with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.
  
For example, if the secret number was 248 and your guess was 843
clues would be Fermi Pico.
'''.format(NUM_LENGTH, 'word' if ALLOW_CHARACTERS else 'number'))

#######################################################
##################################################

    while True:
        secret_number: str = get_secret_num()
        print('I have thought up a number.')
        print(f"You have {NUM_CHANCES} guesses to get it.")
        num_guesses:int=1
        while num_guesses<=NUM_CHANCES:
            guess:str=''
            while len(guess)!=NUM_LENGTH or not guess.isdecimal():
                print(f"Guess #{num_guesses}: ")
                guess=input('> ')
            clues:str=get_clues(guess,secret_number)
            print(clues)
            num_guesses+=1
            if guess==secret_number:
                break
            if num_guesses>NUM_CHANCES:
                print('You ran out of guesses.')
                print(f"The answer was {secret_number}.")
        print('Do you want to play again? (yes or No)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')

def get_secret_num()->str:
    list_of_nums=list('0123456789') # more performance than ```list(range(1,10))```
    characters='abcdefghijklmnopqrstuvwxyz'
    if ALLOW_CHARACTERS:
        list_of_nums.extend(list(characters))
    if ALLOW_UPPER_CHARACTERS:
        list_of_nums.extend(list(characters.upper())) # não encontrei uma maneira mais abstrata de unir várias listas
    random.shuffle(list_of_nums)
    #return ''.join(list_of_nums[:NUM_LENGTH]) # equivalent to ```str.join('',list_of_nums[:3])```
    # more performative than code above ☝️ is:
    result:str=''
    for i in range(NUM_LENGTH):
        result+=list_of_nums[i]
    return result

def get_clues(guess:str,secret_number:str)->str:
    if guess == secret_number:
        return 'You got it!'
    clues:list[str]=[]
    for i in range(len(guess)):
        if guess[i]==secret_number[i]:
            clues.append('Fermi')
        elif guess[i] in secret_number:
            clues.append('Pico')
        #if len(clues)==0:
        # alternative to code above ☝️ is:
    if not clues:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)

if __name__=='__main__':
    main()