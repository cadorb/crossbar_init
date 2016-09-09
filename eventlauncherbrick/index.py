#!/usr/bin/python3
# -*- coding: utf-8 -*

# import cgi 

# form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

# print(form.getvalue("name"))


fichier = open("html.html", "r")
html = fichier.read()


print(html)