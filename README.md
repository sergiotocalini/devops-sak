# DevOps Tools

DevOps Tools is a set of tools to help the DevOps, ItOps or SysAdmin to update manage the infrastructure in an easy way.

# Tools
## dnsquery
Usage
```
#~ dnsquery -h
Usage: dnsquery [options]

Options:
  -h, --help            show this help message and exit
  -G str, --grep=str    Grep output.
  -d str, --domain=str  Domain
  -e str, --environment=str
                        Environment query.
  -f list, --fields=list
                        Display fields (ip, name, type).
  -g str, --game=str    Game query.
  -r str, --regex=str   Regular Expression.
  -s str, --server=str  DNS Server
  -t list, --type=list  Type filter
  --delimiter=str       Delimiter
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
* [IPy](https://pypi.python.org/pypi/IPy)
* [PrettyTable](https://pypi.python.org/pypi/PrettyTable)

# Installation
Download the master branch and install it using setuptools.
```
#~ wget -c "https://github.com/sergiotocalini/devops-tools/archive/master.zip"
#~ unzip master.zip
#~ cd devops-tools-master
#~ sudo python setup.py install
```
