#!/usr/bin/python3
""" parses logs """


import sys


def main():
    """ main func """
    total_file_size = 0
    status_codes_count_map = {
       "200": 0,
       "301": 0,
       "400": 0,
       "401": 0,
       "403": 0,
       "404": 0,
       "405": 0,
       "500": 0
    }
    # while True:
    try:
        count = 0
        for line in sys.stdin:
            tokens = line.split()
            if len(tokens) == 9:
                total_file_size += int(tokens[8])
                count += 1
                status_codes_count_map[tokens[7]] += 1

                if count == 10:
                    count = 0
                    print_report(
                        status_codes_count_map,
                        total_file_size
                    )
                    zero_status_codes_count_map(
                        status_codes_count_map
                    )

    except KeyboardInterrupt:
        print_report(
            status_codes_count_map,
            total_file_size
        )
        # break


def zero_status_codes_count_map(dct_):
    """ reinitializes dct to 0 """
    for key in dct_:
        dct_[key] = 0


def print_report(dct_, file_size):
    """ prints to stdout summary of logs """
    print("File size: {}".format(file_size))
    for key in dct_:
        if dct_[key]:
            print("{}: {}".format(key, dct_[key]))


if __name__ == "__main__":
    main()
