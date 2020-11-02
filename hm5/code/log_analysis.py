import argparse
import os
import re
import sys
from collections import Counter
from operator import itemgetter
from datetime import datetime

import pytest

from orm_client.mysql_orm_client import MysqlOrmConnection
from tests.orm_builder import MysqlOrmBuilder


class ParseLogLine:

    def __init__(self, line):
        self.line = line

    def get_ip_address(self):
        ip_format = ""
        matched = re.search(r"[0-9]+(?:\.[0-9]+){3}", self.line)
        if matched:
            ip_format = matched.group()
        else:
            ip_format = None
        return ip_format

    def get_date(self):
        date_format = ""
        matched = re.search(r"[\d]{2}/[\w]{3}/[\d]{4}:[\d]{2}:[\d]{2}:[\d]{2}", self.line)
        if matched:
            date_format = matched.group()
        else:
            date_format = None
        return date_format

    def get_method(self):
        return self.line.split(' ')[:9][5][1:]

    def get_location(self):
        return self.line.split(' ')[:9][6]

    def get_protocol(self):
        return self.line.split(' ')[:9][7][:-1]

    def get_status_code(self):
        return self.line.split(' ')[:9][8]


class ParseLogFile:

    def __init__(self, file):
        self.file = file

    def get_dicts(self, _lst):
        lst = []
        _dict = {}
        id = 0
        for line in _lst:
            id += 1
            l = ParseLogLine(line)
            _dict['id'] = id
            _dict['ip address'] = l.get_ip_address()
            _dict['protocol'] = l.get_protocol()
            _dict['method'] = l.get_method()
            _dict['location'] = l.get_location()
            _dict['status code'] = l.get_status_code()
            _dict['date'] = l.get_date()
            lst.append(_dict.copy())
        return lst

    def req_cnt_all(self):
        return {
            'log file': str(self.file.name),
            'count of requests': len(list(self.file)),
            'date of call': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }


    def req_cnt_separ(self, method):
        i = 0
        for line in self.file:
            if ParseLogLine(line).get_method() == method:
                i += 1
        return {
            'log file': str(self.file.name),
            'count of requests with method': i,
            'method': method,
            'date of call': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }

    def greatest_req(self):
        _lst = sorted([line for line in self.file.readlines()], key=len, reverse=True)
        leng = [len(l) for l in _lst]
        lst = self.get_dicts(_lst)

        return {
            'log file': str(self.file.name),
            'top 10 greatest requests': [
                {i+1: lst[i], 'length': leng[i]} for i in range(10)
            ],
            'date of call': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }

    def greatest_error_loc(self, code_first_char):
        data = self.get_dicts(self.file)
        req_with_error = [i for i in data if i['status code'].startswith(code_first_char)]
        locs = dict(Counter(x['location'] for x in req_with_error))
        res = sorted(locs.items(), key=itemgetter(1), reverse=True)
        return {
            'log file': str(self.file.name),
            'top 10 greatest requests with error': [
                {i+1: {
                    'location': res[i][0],
                    'count of requests': res[i][1]
                }} for i in range(10)
            ],
            'error type': 'client' if code_first_char == '4' else 'server',
            'date of call': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }

    def is_parseble(self):
        with open(self.file.name, 'r') as file:
            for line in file:
                parsed = ParseLogLine(line)
                if parsed.get_ip_address() is None or parsed.get_date() is None:
                    return False
            return True


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

def options(arg, filename, _mysql, _builder):
    with open(filename, 'r') as file:
        p = ParseLogFile(file)
        if p.is_parseble():
            if arg.command == 'requestcountall' or arg.command == 'a':
                res = p.req_cnt_all()
                main_id = _builder.add_main(file.name, datetime.strptime(
                    res['date of call'],
                    '%d/%m/%Y %H:%M:%S'
                )).id
                _builder.add_count_of_all_requests(res['count of requests'], main_id)
            elif arg.command == 'requestcountsepar' or arg.command == 'm':
                res = p.req_cnt_separ(arg.method)
                main_id = _builder.add_main(file.name, datetime.strptime(
                    res['date of call'],
                    '%d/%m/%Y %H:%M:%S'
                )).id
                _builder.add_count_of_requests_by_method(
                    res['count of requests with method'],
                    arg.method,
                    main_id
                )
            elif arg.command == 'greatestrequests' or arg.command == 'g':
                res = p.greatest_req()
                main_id = _builder.add_main(file.name, datetime.strptime(
                    res['date of call'],
                    '%d/%m/%Y %H:%M:%S'
                )).id
                for d in res['top 10 greatest requests']:
                    k = list(d.keys())[0]
                    _builder.add_greatest_requests(
                        top=k,
                        length=d['length'],
                        ip_address=d[k]['ip address'],
                        protocol=d[k]['protocol'],
                        method=d[k]['method'],
                        location=d[k]['location'],
                        status_code=d[k]['status code'],
                        date=datetime.strptime(
                            d[k]['date'],
                            '%d/%b/%Y:%H:%M:%S'
                        ),
                        main_id=main_id
                    )
            elif arg.command == 'locwithclienterror' or arg.command == 'c':
                res = p.greatest_error_loc('4')
                main_id = _builder.add_main(file.name, datetime.strptime(
                    res['date of call'],
                    '%d/%m/%Y %H:%M:%S'
                )).id
                for d in res['top 10 greatest requests with error']:
                    k = list(d.keys())[0]
                    _builder.add_requests_by_error(
                        top=k,
                        location=d[k]['location'],
                        value=d[k]['count of requests'],
                        error_type=res['error type'],
                        main_id=main_id
                    )
            elif arg.command == 'locwithservererror' or arg.command == 's':
                res = p.greatest_error_loc('5')
                main_id = _builder.add_main(file.name, datetime.strptime(
                    res['date of call'],
                    '%d/%m/%Y %H:%M:%S'
                )).id
                for d in res['top 10 greatest requests with error']:
                    k = list(d.keys())[0]
                    _builder.add_requests_by_error(
                        top=k,
                        location=d[k]['location'],
                        value=d[k]['count of requests'],
                        error_type=res['error type'],
                        main_id=main_id
                    )
            else:
                print('Try --help')
        else:
            print(file.name, " no parseble")


def main():
    arg = parse()
    _mysql: MysqlOrmConnection = MysqlOrmConnection(
        user='root',
        password='passw',
        db_name='LOGGER_DB'
    )
    _builder: MysqlOrmBuilder = MysqlOrmBuilder(connection=_mysql)
    last_arg = arg.filename
    try:
        if os.path.isdir(last_arg):
            for _file in os.listdir(last_arg):
                options(arg, last_arg + _file, _mysql, _builder)
        else:
            options(arg, last_arg, _mysql, _builder)
    except IOError:
        print('No such file or dir')


if __name__ == '__main__':
    main()
