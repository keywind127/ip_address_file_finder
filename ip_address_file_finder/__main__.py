import argparse

from ip_address_file_finder.main import main

parser = argparse.ArgumentParser(description = "This module is used to find all IP address and port numbers of files.")

parser.add_argument("-d", "--directory", help = "Directory to check for IP and PORT.", default = "./")

args = parser.parse_args()

main(args.directory)