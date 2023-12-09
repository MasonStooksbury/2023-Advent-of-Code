#!Python3

def getInput(filepath):
    lines = ''
    with open(f'../Input/{filepath}', 'r') as file:
        lines = file.read()

    return lines.split('\n')
