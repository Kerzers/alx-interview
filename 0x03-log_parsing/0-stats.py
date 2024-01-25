#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import sys


count = 0
size = 0
status_code = ["200", "301", "400", "401", "403", "404", "405", "500"]
code = {"200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0}

try:
    for line in sys.stdin:
        line_args = line.split(" ")
        if len(line_args) > 4:
            size += eval(line_args[-1])
            if line_args[-2] in status_code:
                code[line_args[-2]] += 1
            count += 1

        if count == 10:
            print("File size: {}".format(size))
            for key, values in code.items():
                if values != 0:
                    print("{}: {}".format(key, values))
            count = 0
            code = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
except KeyboardInterrupt:
    pass
