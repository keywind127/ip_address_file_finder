from typing import Iterator, Tuple, List

import argparse

import re

import os

class bcolors(object):
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKCYAN    = '\033[96m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'


def find_files(directory : str) -> Iterator[ str ]:
    for root, _, files in os.walk(directory):
        for file in files:
            filename = os.path.normpath(os.path.abspath(os.path.join(root, file))).replace("\\", "/")
            if (os.path.isfile(filename)):
                yield filename

def find_host_port(filename : str) -> Iterator[ Tuple[ str, int, str ] ]:

    file_lines : List[ str ] = open(filename, "r", -1, "utf-8").read().split("\n")

    for line_idx, file_line in enumerate(file_lines, start = 1):
        for host_port in re.findall("[\d]+\.[\d]+\.[\d]+\.[\d]+\:[\d]+|[\d]+\.[\d]+\.[\d]+\.[\d]+", file_line):
            yield (filename, line_idx, host_port)

def main(directory : str, extension : str) -> None:

    print(f"\n[ SEARCHING ] [ {bcolors.OKGREEN}{directory}{bcolors.ENDC} ]\n")

    for filename in filter(lambda x : ((True) if (extension == "") else (os.path.splitext(x)[1].replace(".", "").lower() == extension.lower())), find_files(directory)):
        try:
            for (_filename, _line_idx, _host_port) in find_host_port(filename):
                print(f"""[ FOUND ] [ {bcolors.OKBLUE}{_line_idx}{bcolors.ENDC} ] [ {bcolors.WARNING}{_host_port}{bcolors.ENDC} ] [ {bcolors.OKGREEN}{_filename}{bcolors.ENDC} ]""")
        except KeyboardInterrupt:
            raise
        except Exception:
            pass
    print("")

if (__name__ == "__main__"):

    parser = argparse.ArgumentParser(description = "This module is used to find all IP address and port numbers of files.")

    parser.add_argument("-d", "--directory", help = "Directory to check for IP and PORT.", default = "./")

    parser.add_argument("-e", "--extension", help = "File extension type. For example, `py`.", default = "")

    args = parser.parse_args()

    main(args.directory, args.extension)