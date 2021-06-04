#!/usr/bin/env python3

import shutil
from argparse import ArgumentParser
from os import path


parser = ArgumentParser()
parser.add_argument("paths", nargs="*", default="./")
args = parser.parse_args()


def check_dir_exists(dir):
    is_it_there = path.exists(dir)
    if not is_it_there:
        print("Path {} does not exist.".format(dir))
        exit()


def format_bytes(size):
    # 2**10 = 1024
    power = 2**10
    n = 0
    labels = {0: 'B', 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB'}
    while size > power:
        size /= power
        n += 1
    return size, labels[n]


def format_print_disk_usage(dir):
    stat = shutil.disk_usage(dir)
    t, labelT = format_bytes(stat[0])
    u, labelU = format_bytes(stat[1])
    f, labelF = format_bytes(stat[2])
    percent = (u * 100 / t)
    print("""{}:\n  total: {:8.2f} {}
  free:  {:8.2f} {}
  used:  {:8.2f} {} ({:0.0f}%)"""
          .format(dir, t, labelT, f, labelF, u, labelU, percent))


def main():
    dir = args.paths
    if isinstance(dir, str):
        check_dir_exists(dir)
        format_print_disk_usage(dir)
    else:
        for d in dir:
            check_dir_exists(d)
            format_print_disk_usage(d)
            print()


if __name__ == "__main__":
    main()
