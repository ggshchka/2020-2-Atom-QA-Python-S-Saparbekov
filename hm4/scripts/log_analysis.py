import argparse
import json
import os
import re
import sys
from collections import Counter
from operator import itemgetter


class ParseLogLine:

    def __init__(self, line):
        self.ip_address = self.get_ip_format(line)
        self.date = self.get_date_format(line)
        self.method = self.get_method(line)
        self.location = self.get_location(line)
        self.protocol = self.get_protocol(line)
        self.status_code = self.get_status_code(line)

    def get_ip_format(self, line):
        ip_format = ""
        matched = re.search(r"[0-9]+(?:\.[0-9]+){3}", line)
        if matched:
            ip_format = matched.group()
        else:
            ip_format = None
        return ip_format

    def get_date_format(self, line):
        date_format = ""
        matched = re.search(r"[\d]{2}/[\w]{3}/[\d]{4}", line)
        if matched:
            date_format = matched.group()
        else:
            date_format = None
        return date_format

    def get_method(self, line):
        return line.split(' ')[:9][5][1:]

    def get_location(self, line):
        return line.split(' ')[:9][6]

    def get_protocol(self, line):
        return line.split(' ')[:9][7][:-1]

    def get_status_code(self, line):
        return line.split(' ')[:9][8]


# ----------------------------

def is_parseble(filename):
    with open(filename, "r") as file:
        for line in file:
            parsed = ParseLogLine(line)
            if parsed.ip_address is None or parsed.date is None:
                return False
    return True

# ----------------------------

def get_dicts(file):
    lst = []
    _dict = {}
    id = 0
    for line in file:
        id += 1
        l = ParseLogLine(line)
        _dict['id'] = id
        _dict['ip address'] = l.ip_address
        _dict['protocol'] = l.protocol
        _dict['method'] = l.method
        _dict['location'] = l.location
        _dict['status scripts'] = l.status_code
        _dict['date'] = l.date
        lst.append(_dict.copy())
    return lst


def req_cnt_all(file):
    return len(list(file))


def req_cnt_separ(file, method):
    i = 0
    for line in file:
        if ParseLogLine(line).method == method:
            i += 1
    return i


def greatest_req(file):
    lst = sorted(list(file), key=len, reverse=True)
    return lst[:10]  # {i+1: lst[i] for i in range(10)}


def greatest_error_loc(file, code_first_char):
    data = get_dicts(file)
    req_with_error = [i for i in data if i['status scripts'].startswith(code_first_char)]
    locs = dict(Counter(x['location'] for x in req_with_error))
    res = sorted(locs.items(), key=itemgetter(1), reverse=True)
    return dict(res[:10])


# ----------------------------------------

def parse():
    parser = argparse.ArgumentParser(description='Analysis log files')
    parser.add_argument(
        'command', help='requestcountall or a, '
                        'requestcountsepar or m, '
                        'greatestrequests or g, '
                        'locwithclienterror or c, '
                        'locwithservererror or s'
    )
    parser.add_argument(
        'method', help='POST, GET, ...', nargs='?'
    )
    parser.add_argument(
        'filename', help='filename or dir'
    )
    return parser.parse_args(sys.argv[1:])


def pretty_printer(write_func, action, name, com, method=''):
    write_func("*************************************************\n")
    write_func('    ' + name)
    write_func('  ' + com + '  ' + method)
    write_func("\n-------------------------------------------------\n")
    write_func(str(action))
    write_func("\n-------------------------------------------------\n\n")


def options(arg, _FILENAME):
    with open("../result/res_python.txt", "a+") as res_file:
        with open(_FILENAME, "r") as file:
            if arg.command == 'requestcountall' or arg.command == 'a':
                pretty_printer(
                    res_file.write,
                    req_cnt_all(file),
                    file.name,
                    arg.command,
                )
            elif arg.command == 'requestcountsepar' or arg.command == 'm':
                pretty_printer(
                    res_file.write,
                    req_cnt_separ(file, arg.method),
                    file.name,
                    arg.command,
                    arg.method
                )
            elif arg.command == 'greatestrequests' or arg.command == 'g':
                pretty_printer(
                    res_file.write,
                    greatest_req(file),
                    file.name,
                    arg.command
                )
            elif arg.command == 'locwithclienterror' or arg.command == 'c':
                pretty_printer(
                    res_file.write,
                    greatest_error_loc(file, '4'),
                    file.name,
                    arg.command
                )
            elif arg.command == 'locwithservererror' or arg.command == 's':
                pretty_printer(
                    res_file.write,
                    greatest_error_loc(file, '5'),
                    file.name,
                    arg.command
                )
            else:
                print('Try --help')


def run():
    arg = parse()
    _FILENAME = arg.filename
    try:
        if is_parseble(_FILENAME):
            if os.path.isdir(_FILENAME):
                for file in os.listdir(_FILENAME):
                    options(arg, _FILENAME+file)
            else:
                options(arg, _FILENAME)
        else:
            print("No parseble")
    except IOError:
        print('No such file or dir')

if __name__ == '__main__':
    run()
