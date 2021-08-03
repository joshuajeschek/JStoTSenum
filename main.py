# RUN THIS FILE TO GET AN INTERFACE WITH THE CONVERTER
from converter import getEnums, saveEnums
from tkinter import Tk
from util import colors, getDir


if __name__ == '__main__':

    print(colors.PURPLE + 'This converter will convert JavaScript enums like this:\n' + colors.RESET +\
        '\thttps://github.com/DoctorMcKay/node-steam-user/blob/master/enums/EAccountType.js\n' +\
        'into TypeScript enums.\n\n' +\
        'JavaScript enums must be directly exported using module.exports this:\n' +\
        '    module.exports = {\n' +\
        '        "FIRST_ENTRY" = 0,\n' +\
        '        "SECOND_ENTRY" = 2\n' +\
        '    }\n\n' +\
        'There can only be one Enum per file.\n\n' +\
        'First, choose a directory with one or more Javascript Files.'
    )
    input('Press Enter...')

    #tkinter prep
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)

    js_directory = getDir('Choose a directory with one ore more Javascript Files')

    print('Next, choose the directory where the TypeScript files should be saved.')
    ts_directory = getDir('Choose the directory where the TypeScript Files should be saved.')

    print('Analyzing JS Files...')
    enums = getEnums(js_directory)

    print('Found the following Enums:\n')
    for name in enums.keys():
        print(f'\t{name}: {len(enums[name])} entries')
    
    print('\n')

    if input('Save these Enums to TypeScript files? [Y, n]: ').lower() == 'n':
        exit()

    saveEnums(ts_directory, enums)
    print(colors.GREEN + 'done.' + colors.RESET)
