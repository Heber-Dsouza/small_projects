from msvcrt import getch

SpecialKeyType={
    "space":"SPACE",
    "esc":"ESC",
    "enter":"ENTER",
    "upper_key":"UPPER_KEY",
    "down_key":"DOWN_KEY",
    "left_key":"LEFT_KEY",
    "right_key":"RIGHT_KEY",
}

def pressed_key(message:str=None,end:str=None)->str:
    if message is not None:
        print(message+" ",end="")
    key=ord(getch())
    if key==27:
        return SpecialKeyType["esc"]
    if key==13:
        return SpecialKeyType["enter"]
    if key==224:
        special_key=ord(getch())
        match special_key:
            case 80:
                return SpecialKeyType["down_key"]
            case 72:
                return SpecialKeyType["upper_key"]
            case _:
                return "UNKNOWN"
    if end is not None:
        print(end)
    return chr(key)