#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pyzufall as z

print("Testscript für die Klasse PyZufall\n")
print("Person: "+z.person())
print("Essen2: "+z.essen(2))
print("Essen: "+z.essen(0))
print("Trinken: "+z.trinken())
print("Ort: "+z.ort())
print("Satz: "+z.satz())

for i in range(1,20):
	print(z.satz())