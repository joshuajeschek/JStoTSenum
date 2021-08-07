from os import listdir
from os.path import isfile, join
from pyjsparser import parse
from util import isInt
from typing import Dict, List, Union

def convertConstToTS(js_dir:str, ts_dir:str):
    files = [f for f in listdir(js_dir) if isfile(join(js_dir, f))]
    js_files = []
    for file in files:
        if file.endswith('.js'):
            js_files.append(file)

    for js_file in js_files:
        name = js_file.replace('.js', '')
        with open(join(js_dir, js_file)) as js_f:
            with open(join(ts_dir, name + '.d.ts'), 'a') as ts_f:
                for line in js_f.readlines():
                    ts_f.write(line.replace('module.exports =', f'declare const {name}:'))
                ts_f.write('\n')
                ts_f.write(f'export = {name}\n')

def saveEnums(dir:str, enums:Dict[str, List[Dict[str, int]]]):
    with open(join(dir, 'all' + '.ts'), 'a') as a:
        for name in enums.keys():
            with open(join(dir, name + '.ts'), 'a') as f:
                f.write('// auto generated Enums\n\n')
                f.write(f'export enum {name} {{\n')
                a.write(f'\nexport enum {name} {{\n')
                for entry in enums[name]:
                    f.write(f'    {entry["key"]} = {entry["value"]},\n')
                    a.write(f'    {entry["key"]} = {entry["value"]},\n')
                f.write('}\n')
                a.write('}\n')


def getEnums(dir:str) -> Dict[str, List[Union[str, int]]]:
    '''
    Extracts Enums from JavaScript Files in a directory
    '''
    files = [f for f in listdir(dir) if isfile(join(dir, f))]
    js_files = []
    for file in files:
        if file.endswith('.js'):
            js_files.append(file)
    
    enums = dict()
    for js_file in js_files:
        with open(join(dir, js_file)) as file:
            content = parse(file.read())
            for expression in content['body']:
                if expression['type'] == 'ExpressionStatement' and \
                    expression['expression']['type'] == 'AssignmentExpression' and \
                    expression['expression']['left']['type'] == 'MemberExpression' and \
                    expression['expression']['right']['type'] == 'ObjectExpression' and \
                    expression['expression']['left']['object']['name'] == 'module' and \
                    expression['expression']['left']['property']['name'] == 'exports':
                    entries = []
                    for entry in expression['expression']['right']['properties']:
                        key = entry['key']['value']
                        try:
                            value = entry['value']['raw']
                        except KeyError:
                            value = entry['value']['operator'] + entry['value']['argument']['raw']

                        if not isInt(key) and isInt(value):
                            entries.append({
                                'key': key,
                                'value': int(value)
                            })

                    enums[js_file.replace('.js', '')] = entries

    return enums

if __name__ == '__main__':
    print('Please run main.py')
