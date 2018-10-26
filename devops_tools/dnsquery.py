#!/usr/bin/env python
import dns.query
import dns.zone
import re
import sys

class DNSQuery():
    def __init__(self, server):
        self._Server = server

    def get_zone(self, domain):
        try:
            zone = dns.zone.from_xfr(dns.query.xfr("%s" %(self._Server),
                                                   "%s" %(domain)))
        except:
            print("Zone doesn't found.")
            exit(1)
        records = sorted(zone.nodes.keys())
        return zone, records

    def get_records(self, opt):
        opt.setdefault('grep', '')
        opt.setdefault('regex', '.*')
        opt.setdefault('type', ['A', 'CNAME'])

        filter_hostname = re.compile(opt['regex'], re.IGNORECASE)

        zone, records = self.get_zone(opt['domain'])
        list_rec = []
        for i in records:
            for x in zone[i].to_text(i).split("\n"):
                row = x.split(" ")
                if (opt['type'] == "*") or (row[3] in opt['type']):
                    if filter_hostname.match(row[0]):
                        if (opt['grep'].lower() in row[0].lower()):
                            hostname = '.'.join([row[0], opt['domain']])
                            list_rec.append(
                                {
                                    'ip':row[4], 'host':hostname,
                                    'type':row[3] , 'ttl':row[1]
                                }
                            )
        return list_rec
                
    def display_output(self, records, options, delimiter):
        base_string = delimiter.join(["%(" + o + ")s" for o in options])
        for d in records:
            for o in options: d.setdefault(o, "")
            print(base_string % d)
    
def main():
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-d", "--domain", dest="domain",
                      default="aws.vostu.com",
                      help="Domain", metavar="str")
    parser.add_option("-f", "--fields", dest="fields", default="ip,host",
                      help="Display fields (ip, name, type).",
                      metavar="list")
    parser.add_option("-r", "--regex", dest='regex', default='.*',
                      help="Regular Expression.", metavar="str")
    parser.add_option("-s", "--server", dest="server", default="dns1",
                      help="DNS Server", metavar="str")
    parser.add_option("-t", "--type", dest="rtype", default="A,CNAME",
                      help="Type filter", metavar="list")
    parser.add_option("-D", "--delimiter", dest="delimiter", default="\t",
                      help="Delimiter", metavar="str")
    (options, args) = parser.parse_args()
    if options.server and options.domain:
        options = {
            'domain': options.domain,
            'type': [t.upper() for t in options.rtype.split(",")],
            'regex': options.regex,
            'server': options.server,
            'delimiter': options.delimiter,
            'fields': [f.lower() for l in options.fields.split(",")]
        }
        DNSAdmin = DNSQuery(options['server'])
        Records = DNSAdmin.get_records(options)
        DNSAdmin.display_output(Records, options['fields'], 
                                options['delimiter'])
    else:
        print("DNSQuery: Required arguments missing or invalid.")
        print(parser.print_help())
        sys.exit(-1)

if __name__ == '__main__':
    main()
