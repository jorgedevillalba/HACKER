#!/usr/bin/python

import urllib

web = raw_input("Ingrese Link: ")
prueba = "'"
url = web + prueba
packet = urllib.urlopen(url)
fuente = packet.read()
error = "SQL syntax"
if error in fuente:
	print url + " Parece ser vulnerable"
else:
	print url + " No parece ser vulnerable"
