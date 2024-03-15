from setuptools import setup

setup(
    name = "ip-address-file-finder",
    version = '0.0.5',
    description = 'This module is used to find files containing IP addresses and PORTs.',
    author = 'keywind127',
    author_email = 'watersprayer127@gmail.com',
    url = 'https://github.com/keywind127/ip_address_file_finder',
    packages = [ "ip_address_file_finder" ],
    install_requires = [
        'Markdown',
    ],
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)