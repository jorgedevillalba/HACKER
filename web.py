#!/usr/bin/python

import urllib

web = raw_input("Ingrese el dominio: ")

try:
	a = "/robots.txt"
	url = "http://" + web + a
	packet = urllib.urlopen(url)
	if packet.code  == 200:
		msg = "Si tiene Robots"
		robot = packet.read()
		print msg
		print robot
	else:
		msg = "No tiene robots"
		print msg


except:
	msg = "Host esta down"
	print msg
