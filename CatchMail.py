# -*- coding: utf-8 -*-
# @Author: Ph0rse

import time
import sys
import os
import errno
from io import StringIO
from datetime import datetime
import optparse
import json
import traceback
import requests
from pyfiglet import Figlet


__VERSION__ = "0.1"

__TOKEN__ = "0kee.token"

__URL__ = "https://api.0kee.com/api/email/query/"

def haveError(data):
    if 'error' in data:
        print(">>> Failed!!")
        print(">>> "+data['error'])
        return True
    return False

def showPage():
    f = Figlet(font='slant')
    print(f.renderText('CatchMail'))

def formatOut(data):
    print(">>> Hello "+data["user"])
    print(">>> Successful.")
    print(">>> Your balance : %d" % data['Balance'])
    print(">>> Got %d email:\n" % data['count'])
    
    for email in data['result']:
        print(email[0])

def getEmail(token):
    # payload = {'domain': options.domain,'limit': options.limit, 'start':options.start, 'token':token}
    payload = {'domain': options.domain,'limit': options.limit, 'token':token}
    res = requests.post(url=__URL__,data= payload)
    print(res)
    return res.json()

def usage():
    s = StringIO()
    s.write("Usage:  %s <domain> [type] [options]\n" %sys.argv[0])
    s.write("\t./python3 CatchMail.py -d 360.cn\n")
    s.write("\t./python3 CatchMail.py -d 360.cn -o out.json\n")
    s.write("\t./python3 CatchMail.py -d 360.cn -l 100\n")
    # s.write("\t./python3 CatchMail.py -d 360.cn -s 100 -l 100\n")
    s.seek(0)
    return s.read()

def parse_option():
    parser = optparse.OptionParser(usage=usage())
    parser.add_option("-v", "--version", action="store_true", dest="version")
    parser.add_option("-d", "--domain", action="store", type="string", default="null", dest="domain",help="domain of email")    
    parser.add_option("-l", "--limit", action="store", type="int", default=100, dest="limit",
                    help="limit number of results. [default: %default]")
    parser.add_option("-o", "--outfile", dest="out", type="string", default="null",action="store", 
                    help="output into file")

    # parser.add_option("-s", "--start", action="store", type="int", default="0", dest="start")


    return parser

def main():
    global options, args
    parser = parse_option()
    options, args = parser.parse_args()

    if options.version:
        print("CatchMail %s" %__VERSION__)
        sys.exit(0)
    if (options.domain == "null"):
        parser.print_help()
        sys.exit(1)
    try:
        token = open(__TOKEN__,'r').read().strip()
    except Exception as e:
        sys.stderr.write("%s\n" %e.message)
        sys.exit(1)

    showPage()
    data = getEmail(token)

    if options.out != "null":
        print(">>> Hello "+data["user"])
        print(">>> Successful.")
        print(">>> Your balance : %d" % data['Balance'])
        print(">>> Got %d email:\n" % data['count'])
        print(">>> Imported into "+options.out)
        with open(options.out,'w') as outFile:
            for emailaddr in data['result']:
                outFile.write(emailaddr[0]+'\n')
    else:
        if haveError(data):
            exit()
        formatOut(data)
    


if __name__ == "__main__":
    main()