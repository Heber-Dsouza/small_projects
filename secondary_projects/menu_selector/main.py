from classes import Screen
from utils import pressed_key

def main():
    x=pressed_key("message:",end='')
    print(x)

if __name__=='__main__':
    main()