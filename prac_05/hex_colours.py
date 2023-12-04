CODE_TO_NAME = {'APRICOT': '#fbceb1', 'AQUA': '#00fff', 'BEAVER': '	#9f8170', 'BEIGE': '#f5f5dc',
                'BITTERSWEET': '#fe6f5e', 'BLACK': '#000000', 'BLOND': '#faf0be', 'BOLE': '#79443b', 'BRASS': '#b5a642',
                'BRONZE': '#cd7f32'}
print(CODE_TO_NAME)

color_name = input('Enter color name: ').upper()
while color_name != '':
    try:
        print(color_name, 'is', CODE_TO_NAME[color_name])
    except KeyError:
        print('Invalid color name')
    color_name = input('Enter color name: ').upper()

for color_name, color_code in CODE_TO_NAME.items():
    print(f'color code of {color_name} is {color_code}')


