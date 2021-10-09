# !/usr/bin/python3

# gnome keyring does not like ./hn2md.py execution,
# so you need to run this script like 
#       python3 internsupp.py

import keyring as kring
import requests
from bs4 import BeautifulSoup as bsoup
import html
import re
import time
import subprocess as subp
import sys
import os

# show usage
def show_usage():
    print("Usage: python3 hn2md.py [MAXPAGE]")
    print("\tMAXPAGE:\t\toptional, integer value, if none is given then all pages will be fetched.")

# get the string enclosed in <a></a>
def get_title(string):
    s = re.findall('<a.*?>(.+?)</a>', string)
    return html.unescape(s[0]).strip() if len(s) > 0 else None

# get the company name
def get_name(string):
    name = re.findall('<li>(.+?)<', string)[0].split(">")[0]
    # print(name)
    return html.unescape(name).strip()

# fetch all entries from www.intern.supply
def fetch_entries():
    nontitle = ["Software", "Design", "Newsletter", "Staff Picks", "Sponsor", \
            "contact@intern.supply<br><br/></br>"]
    url = 'http://www.intern.supply/'
    response  = requests.get(url)
    soup = bsoup(response.content.decode('utf-8', 'ignore'), 'html.parser')
    lst = soup.find_all("li")
    entries = []
    for item in lst: 
        itemstr = str(item).strip()
        if get_title(itemstr) not in nontitle:
            entries.append(itemstr)
    return entries

# parse all the fetched entries.
def parse_entries(entries):
    ht = {}
    for item in entries:
       name = get_name(item)
       title = get_title(item)
       ht[str(name)] = str(title)
    return ht

# save the dictionary into file
def save_table(ht):
    fh = open("home/khaled/Dropbox/personal/job-app/us/interns/2019/list.txt", "w")
    for key in ht:
        fh.write("{0:s}\t\t\t{1:s}\n".format(key, ht[key]))
    fh.close()

# load the previously saved dictionary
def load_saved_table():
    ht = {}
    try:
        with open("home/khaled/Dropbox/personal/job-app/us/interns/2019/list.txt") as f:
            for line in f:
                string = [x.strip() for x in line.split()]
                button = string[-1]
                if(len(string) > 2):
                    name = " ".join(string[0:-1]).strip()
                else:
                    name = string[0]
                ht[name] = button
    except:
        print("Error: well darn, looks like \'list.txt\' does not exist.", file = sys.stderr)
        sys.exit(1)
    return ht

# find if there is any diff between the old saved table and 
# the newly fetched table
def diff_status(oldt, newt, diffs):
    for key in oldt:
        if oldt[key] != newt[key]:
            diffs[key] = [oldt[key], newt[key]]
    if len(diffs) > 0:
        return True
    else:
        return False

# check if new company name is added or removed
def list_changed(oldt, newt, changed):
    ok = oldt.keys()
    nk = newt.keys()
    if len(ok) != len(nk):
        changed = list(set(ok) & set(nk))
        return True
    else:
        return False



# main
if __name__ == '__main__':
    print("Loading saved entries ...") 
    old_table = load_saved_table()
    # print(old_table)
    print("Fetching new entries from http://www.intern.supply ...")
    entries = fetch_entries()
    new_table = parse_entries(entries)
    # print(new_table)
    # save_table(new_table)
    diffs = {}
    changed = []
    if diff_status(old_table, new_table, diffs) or \
            list_changed(old_table, new_table, changed):
        save_table(new_table)
        print("Status changed:")
        for key in diffs:
            print("\t{0:s}: {1:s} --> {2:s}".format(key, diffs[key][0], diffs[key][1]))
        print("New company added/removed: ", changed)
    else:
        print("No update.")
