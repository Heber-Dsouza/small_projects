from classes import ScreenManager,Screen
from utils import pressed_key

def main():
    screen01=Screen(name="A",state_number=1)
    screen02=Screen(name="B",state_number=2)
    screen03=Screen(name="C",state_number=3)
    screen04=Screen(name="D",state_number=4)

    screen_manager=ScreenManager([screen01,screen02,screen03,screen04],title="Bem-vindo!!!")
    screen_manager.start()

if __name__=='__main__':
    main()