#!/usr/bin/python3
""" parses logs """


import sys


def main():
    """ main func """
    total_file_size = 0
    order = [
       "200",
       "301",
       "400",
       "401",
       "403",
       "404",
       "405",
       "500"
    ]
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
                        total_file_size,
                        order
                    )

    except KeyboardInterrupt:
        print_report(
            status_codes_count_map,
            total_file_size,
            order
        )


# def print_report(dct_, file_size, order):
#     """ prints to stdout summary of logs """
#     print("File size: {}".format(file_size))
#     for key in order:
#         if dct_.get(key):
#             print("{}: {}".format(key, dct_[key]))


def print_report(dct_, file_size, order):
    """ prints to stdout summary of logs """
    report = "File size: {}\n".format(file_size)
    for key in order:
        if dct_.get(key):
            report += "{}: {}\n".format(key, dct_[key])
    report = report[:-1]
    print(report)


if __name__ == "__main__":
    main()
