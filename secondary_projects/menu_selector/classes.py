from os import system
from utils import pressed_key,SpecialKeyType

class Screen:
    def __init__(self,**kwargs):
        self.name:str=kwargs.get("name", "unknown")
        self.state_number:int|None=kwargs.get("state_number",None)
        self.state_children_numbers:list[int]=kwargs.get("state_children_numbers",[])

class ScreenManager:
    __default_custom_selection_helper__:str="pressione as setas cima ou baixo para selecionar opções: "

    def __init__(self,screens:list[Screen],**kwargs):
        self.screens:list[Screen]=screens
        self.title:str|None=kwargs.get("title",None)
        self.custom_selection_helper:str=kwargs.get("custom_selection_helper",self.__default_custom_selection_helper__)

    def start(self)->None:
        screens_length=len(self.screens)
        if screens_length==0:
            print('adicione telas para continuar')

        # if len(self.screens)>1 and True:
        #     pass

        current_index:int=0
        while True:
            system('cls')
            if self.title is not None:
                print(self.title)
                print()

            current_selected:int=self.screens[current_index].state_number
            for item in self.screens:
                print(f"[{'*' if current_selected==item.state_number else ' '}] {item.name}")

            print()
            print(self.custom_selection_helper,end="")

            pressed=pressed_key()
            if pressed==SpecialKeyType["down_key"]:
                current_index=(current_index+1)%screens_length

            if pressed==SpecialKeyType["upper_key"]:
                current_index=(current_index-1)%screens_length