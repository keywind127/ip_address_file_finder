import argparse

from ip_address_file_finder.main import main

parser = argparse.ArgumentParser(description = "This module is used to find all IP address and port numbers of files.")

parser.add_argument("-d", "--directory", help = "Directory to check for IP and PORT.", default = "./")

parser.add_argument("-e", "--extension", help = "File extension type. For example, `py`.", default = "")

parser.add_argument("-f", "--filter", help = "Filter by IP address prefixes. For example, `140.116`.", default = "")

args = parser.parse_args()

main(args.directory, args.extension, args.filter)