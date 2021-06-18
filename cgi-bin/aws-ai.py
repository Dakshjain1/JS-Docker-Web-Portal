#!/usr/bin/python3

print("content-type:text/html")
print()

import cgi

y = cgi.FieldStorage()
x = y.getvalue("name")
print("hi ", x)
