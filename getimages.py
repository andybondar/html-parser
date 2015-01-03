#!/usr/bin/python

url_base = "http://army.lv/large-photos/btr/"
pg = 20


for i in range(pg):
    url = url_base + `i+1`
    print url