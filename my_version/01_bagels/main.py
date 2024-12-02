import random

num_length:int=3

def main():
    print(get_secret_num())
    print(type(get_secret_num()))

def get_secret_num()->str:
    list_of_nums=list('0123456789') # more performance than ```list(range(1,10))```
    random.shuffle(list_of_nums)
    return ''.join(list_of_nums[:num_length]) # equivalent to ```str.join('',list_of_nums[:3])```

if __name__=='__main__':
    main()