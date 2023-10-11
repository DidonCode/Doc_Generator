import os
import sys

import Documentation

def quit(message):
	print(message)
	exit(0)

if not os.path.exists("output"):
	os.mkdir("output")

path = ""

if len(sys.argv) >= 2:
	path = sys.argv[1]
else:
	path = input("Chemin du projet: ")

if not os.path.exists(path):
	quit("Indicate paht not exist")

files = os.listdir(path)
projectName = os.path.splitext(os.path.basename(path))[0]

for file in files:
	if(os.path.isfile(file)):
		documentation = Documentation.documentation(open(file, "r"), projectName, open("other/template.css", "r"), open("other/utility.js", "r"))