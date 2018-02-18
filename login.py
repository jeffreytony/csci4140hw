#!/usr/bin/python

import os
import cgi
import cgitb
import subprocess
import sys



print "Content-Type: text/html"
print

cgitb.enable()

form = cgi.FieldStorage()

user = form.getvalue('login', None)

try:
    passwd = form.getlist('passwd')[0]
except IndexError:
    # No password typed in
    passwd = None

print '<html><body>'