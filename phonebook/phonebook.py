import json
import os
import sys

def load(fname):
    with open(fname) as file:
        return json.load(file)

def dump(data, fname):
    with open(fname, 'w') as file:
        json.dump(data, file)

def create_phonebook(pb_name):
    """create new phonebook"""
    if os.path.exists(pb_name):
        print('File {} already exists.'.format(pb_name), file=sys.stderr)
    else:
        dump({}, pb_name)

def add_entry(name, number, pb_name):
    """add  a new name and number to the given phonebook"""
    d = load(pb_name)
    if name in d:
        print('Name already in {}'.format(pb_name), file=sys.stderr)
    else:
        d[name] = number
        dump(d, pb_name)

def update(name, number, pb_name):
    """ update name or number in the given phonebook"""
    d = load(pb_name)
    if name not in d:
        print('Name not in {}'.format(pb_name), file=sys.stderr)
    else:
        d[name] = number
        dump(d, pb_name)

def lookup(name, pb_name):
    """find the number matching to the given name"""
    d = load(pb_name)
    for key in d:
        if name.lower() in key.lower():
            print(key, d[key])

def reverse_lookup(number, pb_name):
    """find the number matching to the given number"""
    d = load(pb_name)
    for key, value in d.items():
        if number in value:
            print(key, value)

def delete(name, pb_name):
    """ delete the entry from the given phonebook"""
    d = load(pb_name)
    if name not in d:
        print('Name not in {}'.format(pb_name), file=sys.stderr)
    else:
        del d[name]
        dump(d, pb_name)

if __name__ == '__main__':
    args = sys.argv[:]
    script = args.pop(0) # name of the script
    if len(args) == 2:
        command = 'lookup'
    else:
        command = args.pop(0) # main command

    if command == 'create':
        pb_name = args.pop(0)
        create_phonebook(pb_name)

    elif command == 'add':
        name = args.pop(0)
        number = args.pop(0)
        pb_name = args.pop(0)
        add_entry(name, number, pb_name)

    elif command == 'update':
        name = args.pop(0)
        number = args.pop(0)
        pb_name = args.pop(0)
        update(name, number, pb_name)

    elif command == 'lookup':
        name = args.pop(0)
        pb_name = args.pop(0)
        lookup(name, pb_name)

    elif command == 'reverse-lookup':
        number = args.pop(0)
        pb_name = args.pop(0)
        reverse_lookup(number, pb_name)

    elif command == 'delete':
        name = args.pop(0)
        pb_name = args.pop(0)
        delete(name, pb_name)

    else:
        print('Error: unrecognized command', file=sys.stderr)
        sys.exit(-1)
