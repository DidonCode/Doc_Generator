import Generator

class documentation():
    def __init__(self, file, projectName, css, javascript):
        self.output = open("output/temp.html", "w") 
        self.projectName = projectName
        self.css = css
        self.javascript = javascript

        self.generator = Generator.generator(file)
        self.generator.readFile()

        self.start()
        self.createHeadFile()
        self.createBodyFile()
        self.createCssFile()
        self.createJsFile()
        self.finish()

    def start(self):
        self.write("<html>")

    def createHeadFile(self):
        self.write("<head>")
        self.write("<title>Documentation " + self.projectName + "</title>")
        self.write("</head>")

    def createBodyFile(self):
        self.write("<body>")
        lines = self.generator.getParseXml()
        for line in lines:
            self.write(line)
        self.write("</body>")

    def createCssFile(self):
        self.write("<style>")
        lines = self.css.readlines()
        for line in lines:
            self.write(line)
        self.write("</style>")

    def createJsFile(self):
        self.write("<script>")
        lines = self.javascript.readlines()
        for line in lines:
            self.write(line)
        self.write("</script>")

    def finish(self):
        self.write("</html>")

    def write(self, line):
        self.output.write(line + "\n")


