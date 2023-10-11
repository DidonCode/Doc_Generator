import os
import sys

class Doc():
	def __init__(self, inputFileName, inputFileExtension):
		self.inputFileName = inputFileName
		self.inputFileExtension = inputFileExtension

		self.inputFile = open(inputFileName + "." + inputFileExtension, "r")
		self.outputFile = open("output/" + inputFileName + ".html", "w")
	
	def prepare(self):
		self.outputFile.write("<html> \n<head> \n<title>" + self.inputFileName + "." + self.inputFileExtension + "</title> \n</head> \n<body> \n<div class='main'> \n<div class='main-panel'>")

	def generate(self):
		self.outputFile.write("<h1 class='documentation-title'>Documentation</h1>")

		lines = self.inputFile.readlines()

		newFonct = False
		title = ""
		params = []
		desc = "" 
		returned = ""

		self.categorys = []
		categoryBuf = []

		for line in lines:
			if "@func" in line:
				if not newFonct:
					newFonct = True
					self.outputFile.write('<div class="panel"> \n')

				elif newFonct:
					self.outputFile.write('<h3 class="title">' + title + '(')
					for i in range(0, len(params)):
						if(i == len(params) - 1):
							self.outputFile.write(params[i])
						else:
							self.outputFile.write(params[i] + ",")
					self.outputFile.write(')</h3> \n')

					self.outputFile.write('<h4 class="description">' + desc + '</h4> \n')
					self.outputFile.write('<h5 class="return">return ' + returned + '</h5> \n')
					self.outputFile.write("</div> \n")

					newFonct = False
					title = ""
					params = []
					desc = ""
					returned = ""

			if "@param" in line:
				param = line.split("@param")[1]
				params.append(param)

			if "@name" in line:
				if not title:
					title = line.split("@name")[1]
					categoryBuf.append(title)

			if "@desc" in line:
				if not desc:
					desc = line.split("@desc")[1]

			if "@return" in line:
				if not returned:
					returned = line.split("@return")[1]

			if "@category" in line:
				print(line)
				category = line.split("@category")[1]
				if(len(categoryBuf) > 1):
					print(categoryBuf)
					self.categorys.append(categoryBuf)
					categoryBuf = []
				categoryBuf.append(category)

	def finish(self):
		self.outputFile.write("</div> \n")
		
		self.outputFile.write('<div class="side-menu">')
		
		for category in self.categorys:
			self.outputFile.write("<h3 class='category'>" + category[0] + "</h3>")
			for i in range(1, len(category)):
				self.outputFile.write("<h4 class='under-category'>" + category[i] + "</h4>")

		self.outputFile.write("</div> \n")

		self.outputFile.write("</div> \n")


		#---------------------#

		self.outputFile.write("</body> \n</html> \n")

		#---------------------#

		lines = open("other/template.css")

		if lines:
			self.outputFile.write("<style> \n")
			for line in lines:
				self.outputFile.write(line)

			self.outputFile.write("\n</style>")

		#---------------------#

		lines = open("other/utility.js")

		if lines:
			self.outputFile.write("\n <script> \n")
			for line in lines:
				self.outputFile.write(line)

			self.outputFile.write("\n</script>")

if not os.path.exists("output"):
	os.mkdir("output")

fileName = ""
extension = ""

if len(sys.argv) >= 2:
	fileName = sys.argv[1]
	extension = sys.argv[2]
else:
	fileName = input("Nom du fichier: ")
	extension = input("Exension: ")

doc = Doc(fileName, extension)
doc.prepare()
doc.generate()
doc.finish()