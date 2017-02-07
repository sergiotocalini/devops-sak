#!/usr/bin/env python
import dns.query
import dns.zone
import re
import sys
from optparse import OptionParser

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
        records = zone.nodes.keys()
        records.sort()
        return zone, records

    def get_records(self, opt):
        opt.setdefault('environment', None)
        opt.setdefault('grep', '')
        opt.setdefault('regex', '.*')
        opt.setdefault('subdomain', '')
        opt.setdefault('type', ['A', 'CNAME'])

        if opt['environment'] != None:
            opt['domain'] = '%(environment)s.%(domain)s' %opt

        filter_subdomain = re.compile('.*%s$' %opt['subdomain'], re.IGNORECASE)
        filter_hostname = re.compile(opt['regex'], re.IGNORECASE)

        zone, records = self.get_zone(opt['domain'])
        list_rec = []
        for i in records:
            for x in zone[i].to_text(i).split("\n"):
                row = x.split(" ")
                if filter_subdomain.match(row[0]):
                    if (opt['type'] == "*") or (row[3] in opt['type']):
                        if filter_hostname.match(row[0]):
                            if (opt['grep'].lower() in row[0].lower()):
                                hostname = '.'.join([row[0], opt['domain']])
                                list_rec.append({'ip':row[4], 'host':hostname,
                                                 'type':row[3] , 'ttl':row[1]})
        return list_rec
                
    def display_output(self, records, options, delimiter):
        base_string = delimiter.join(["%(" + o + ")s" for o in options])
        for d in records:
            for o in options: d.setdefault(o, "")
            print(base_string % d)

def main(server, env, domain, sub, rtype, delimiter, fields, grep, regex):
    options = {'domain':domain, 'subdomain':sub, 'type':rtype,
               'grep':grep, 'regex':regex, 'environment':env}
    DNSAdmin = DNSQuery(server)
    Records = DNSAdmin.get_records(options)
    DNSAdmin.display_output(Records, fields, delimiter)
    
if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-G", "--grep", dest="grep", default='',
                      help="Grep output.", metavar="str")
    parser.add_option("-d", "--domain", dest="domain", default="aws.vostu.com",
                      help="Domain", metavar="str")
    parser.add_option("-e", "--environment", dest="env", default=None,
                      help="Environment query.", metavar="str")
    parser.add_option("-f", "--fields", dest="fields", default="ip,host",
                      help="Display fields (ip, name, type).", metavar="list")
    parser.add_option("-g", "--game", dest="sub", default='',
                      help="Game query.", metavar="str")
    parser.add_option("-r", "--regex", dest='regex', default='.*',
                      help="Regular Expression.", metavar="str")
    parser.add_option("-s", "--server", dest="server", default="dns1",
                      help="DNS Server", metavar="str")
    parser.add_option("-t", "--type", dest="rtype", default="A,CNAME",
                      help="Type filter", metavar="list")
    parser.add_option("--delimiter", dest="delimiter", default="\t",
                      help="Delimiter", metavar="str")
    (options, args) = parser.parse_args()
    if options.server and options.domain:
        main(options.server, options.env, options.domain,
             options.sub, options.rtype.split(","), options.delimiter,
             options.fields.split(","), options.grep, options.regex)
    else:
        print("DNSQuery: Required arguments missing or invalid.")
        print(parser.print_help())
        sys.exit(-1)
