class Screen:
    def __init__(self,**kwargs):
        self.name:str=kwargs.get("name", "unknown")
        self.state_number:int|None=kwargs.get("state_number",None)
        self.state_children_numbers:list[int]=kwargs.get("state_children_numbers",[])

class ScreenManager:
    def __init__(self,screens:list[Screen]):
        self.screens=screens

    def start(self)->None:
        if len(self.screens)==0:
            print('adicione telas para continuar')

        # if len(self.screens)>1 and True:
        #     pass