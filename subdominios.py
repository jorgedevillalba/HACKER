#!/usr/bin/python

import urllib
import re

url = raw_input("ingresa una url: ") # http://escuela.it/index.php
dominio = raw_input("ingresa el dominio: ") # escuela.it

dominios = []

patron = "https?://([0-9a-zA-Z-_.]+)"
web = urllib.urlopen(url).read()
urls = re.findall(patron, web)

for extraida in urls: #http://escuela.it/dsfsd.html
	if dominio in extraida and extraida not in dominios:
		dominios.append(extraida)

dominios.sort()
print "Subdominios obtenidos:"
for subdominio in dominios:
	print "[+] " + subdominio
