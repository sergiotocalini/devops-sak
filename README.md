# DevOps Swiss Army Knife

[![PyPI version](https://badge.fury.io/py/devops-sak.svg)](https://badge.fury.io/py/devops-sak)
[![Repository License](https://img.shields.io/badge/license-GPLv3-brightgreen.svg)](LICENSE)

DevOps Swiss Army Knife is a set of tools to help the DevOps, ItOps or SysAdmin to update manage the infrastructure in an easy way.

# Tools
## dnsquery
Usage
```
#~ dnsquery -h
Usage: dnsquery.py [options]

Options:
  -h, --help            show this help message and exit
  -d str, --domain=str  Specify the domain.
  -f list, --fields=list
                        Display fields (ip, name, type).
  -r str, --regex=str   Regular Expression.
  -s str, --server=str  DNS Server
  -t list, --type=list  Type filter
  -D str, --delimiter=str
                        Delimiter
#~ 
```

## lanreporter
Usage
```
# lanreporter -h
Usage: lanreporter [action] [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -f FIELDS, --fields=FIELDS
                        Display fields (ip, name, type).
  -o OUTPUT, --output=OUTPUT
                        Output format:filename (default=stdout).
  -s SOURCES, --sources=SOURCES
                        Update domain list.
#~
```

Example
```
#~ lanreporter -s 192.168.122.0/24
+-----------------+-------------------+-----------------+
| ipv4            | mac               | hostname        |
+-----------------+-------------------+-----------------+
| 192.168.122.1   | 00:16:3E:7B:A2:78 |                 |
| 192.168.122.166 |                   | centos7.default |
+-----------------+-------------------+-----------------+
#~
```
# Dependencies
## Operative System
* pip
* [nmap](https://nmap.org/)

## Python libraries
* [dnspython](https://pypi.org/project/dnspython)
* [IPy](https://pypi.python.org/pypi/IPy)
* [PrettyTable](https://pypi.python.org/pypi/PrettyTable)

# Installation
Download the master branch and install it using setuptools.

__**Source**__
```
#~ wget -c "https://github.com/sergiotocalini/devops-sak/archive/master.zip"
#~ unzip master.zip
#~ cd devops-sak-master
#~ sudo pip install .
```

__**PyPi**__
```
~# sudo pip install devops-sak
~#
```
