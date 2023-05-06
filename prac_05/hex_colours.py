CODE_TO_NAME = {"AMBER": "#ffbf00", "Aqua": "#00ffff", "BEAVER": "#9f8170", "BLACK": "#000000", "BLOND": "#faf0be",
                "BOLE": "#79443b", "BRASS": "#b5a642", "CANARY": "#ffff99", "CELADON": "#ace1af"}
print(CODE_TO_NAME)

color_name = input("Enter color: ").upper()
while color_name != "":
    if color_name in CODE_TO_NAME:
        print(f'the code color of {color_name} is {CODE_TO_NAME[color_name]}')
    else:
        print('Invalid')
    color_name = input("Enter color: ").upper()