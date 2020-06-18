#!/bin/python3


import http.client
import sys
print("\n")
print("="*50)
print("Verify if a specific resource exsists in a webserver.")
print("="*50)
print("@elbee_ez or @AstraCyber on twitter.")
print("="*50)

host = input("IP/host: ")
port = input("Port (default is 80): ")
resource = input("Resource to check: ")

chars = set("/.\\") #Used to check resource and host for these characters


if port == "":
	port = 80

#ERROR CHECKING STARTS

if resource == "":
	print("Resource can't be empty.")
	sys.exit()

if any((c in chars) for c in resource):
	print("\n")
else:
	print("Invalid resource. eg. /robots.txt")
	sys.exit()
	
if host == "":
	print("Host can't be empty.")
	sys.exit()
if any((c in chars) for c in host):
	print("\n")
else:
	print("Invalid host. eg. example.com or 127.0.0.1")
	sys.exit()

#ERROR CHECKING ENDS

try:
	connection = http.client.HTTPConnection(host, port)
	connection.request('GET', resource)
	response = connection.getresponse()
	code = str(response.status)
	if code[0] == "2":
		print("\n")
		print("!"*50)
		print("Code ",code)
		print("Resource exsists!")
		print("!"*50)
		print("\n")
	elif code == "404":
		print("Does not exsist!")
	else:
		print("\n")
		print("Code ",code)
		print(response.reason,":(")
		print("\n")


except ConnectionRefusedError:
	print("Connection failed!")
except KeyboardInterrupt:
	print("Cancelled!")

