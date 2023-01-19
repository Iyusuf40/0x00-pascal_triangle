#!/usr/bin/python3
""" parses logs """


import sys


def main():
    """ main func """
    total_file_size = 0
    status_codes_count_map = {"200": 0, "301": 0, "400": 0, "401": 0,
                              "403": 0, "404": 0, "405": 0, "500": 0}
    try:
        count = 0
        for line in sys.stdin:
            count += 1
            tokens = line.split()
            if len(tokens):
                try:
                    total_file_size += int(tokens[-1])
                    status_codes_count_map[tokens[-2]] += 1
                except Exception:
                    pass
                if count == 10:
                    count = 0
                    print_report(
                        status_codes_count_map,
                        total_file_size
                    )
        print_report(status_codes_count_map, total_file_size)

    except KeyboardInterrupt:
        print_report(status_codes_count_map, total_file_size)
        raise


def print_report(dct_, file_size):
    """ prints to stdout summary of logs """
    print("File size: {}".format(file_size))
    for key in sorted(dct_.keys()):
        if dct_.get(key):
            print("{}: {}".format(key, dct_[key]))


if __name__ == "__main__":
    main()
