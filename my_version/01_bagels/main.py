import random

NUM_LENGTH:int=3
NUM_CHANCES:int=8
ALLOW_CHARACTERS:bool=False
ALLOW_UPPER_CHARACTERS:bool=False

def main():
    secret_number:str=get_secret_num()
    for _ in range(NUM_CHANCES):
        user_guess:str=input()
        print(get_clues(user_guess, secret_number))

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
    print('debug',guess,secret_number)
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