#!/usr/bin/python

import urllib

web = raw_input("Ingrese el dominio: ")
archivos = ['/admin.php','/pruebas','/robots.txt', '/xmlrpc.php']

for archivo in archivos:
	url = "http://" + web + archivo
	packet = urllib.urlopen(url)
	if packet.code  == 200:
		msg = "si existe " + archivo
		print msg
	else:
		msg = "No existe " + archivo
		print msg
