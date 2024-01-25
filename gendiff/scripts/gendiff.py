#!/usr/bin/env python3
from gendiff import generate_diff
from gendiff import parse


def main():
    file1, file2 = parse()
    diff = generate_diff(file1, file2)
    print(diff)


if __name__ == '__main__':
    main()
