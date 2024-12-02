from msvcrt import getch
from winsound import Beep

SpecialKeyType={
    "space":"SPACE",
    "esc":"ESC",
    "enter":"ENTER",
    "back_space": "BACK_SPACE",
    "upper_key":"UPPER_KEY",
    "down_key":"DOWN_KEY",
    "left_key":"LEFT_KEY",
    "right_key":"RIGHT_KEY",
}

def pressed_key(message:str=None,end:str=None,enable_beep:bool=True)->str:
    if message is not None:
        print(message+" ",end="")
    key=ord(getch())
    if enable_beep:
        Beep(2000,50)
    if end is not None:
        print(end)
    if key==27:
        return SpecialKeyType["esc"]
    if key==13:
        return SpecialKeyType["enter"]
    if key==32:
        return SpecialKeyType["space"]
    if key==8:
        return SpecialKeyType["back_space"]
    if key==224:
        special_key=ord(getch())
        match special_key:
            case 80:
                return SpecialKeyType["down_key"]
            case 72:
                return SpecialKeyType["upper_key"]
            case 77:
                return SpecialKeyType["right_key"]
            case 75:
                return SpecialKeyType["left_key"]
            case _:
                print(special_key)
                return "UNKNOWN"
    return chr(key)