#!/usr/bin/python
# -*- coding: utf-8 -*-

fichero_pass = open ("/etc/passwd")
linea = fichero_pass.readline
for linea in fichero_pass :
	lista = linea.split(":")
	print lista[0],lista[-1][:-1] #lista[:-1] afecta al resultado de lista[-1]
	# print lista[0],lista[-1],   #otra forma 	

print len(linea)


