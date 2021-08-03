from tkinter import filedialog

class colors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# needs tkinter prep
def getDir(title:str) -> str:
    directory = filedialog.askdirectory(title=title)

    if not directory:
        print(colors.RED + '\nYou did not choose a valid directory' + colors.RESET)
        exit()

    print(f'\nYou chose: {directory}')

    return directory

def isInt(inp) -> bool:
    try:
        int(inp)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    print('Why would you run the util file?')
