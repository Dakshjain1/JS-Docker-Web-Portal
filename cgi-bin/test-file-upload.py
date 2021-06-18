#!/usr/bin/python3

print("content-type:text/html\n\n")

import cgi
import cgitb; cgitb.enable()
import os

form = cgi.FieldStorage()

fileitem = form["filename"]

if fileitem.filename:
  fn = os.path.basename(fileitem.filename)
  open(fn,'wb').write(fileitem.file.read())
  msg = "uploaded"
  print(msg)

else:
  msg = "not uploaded"
  print(msg)
