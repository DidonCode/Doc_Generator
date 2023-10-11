import os

class generator():
    def __init__(self, file):
        self.file = file
        self.parseXml = []

    def readFile(self):
        lines = self.file.readlines()

        for i in range(0, len(lines)):
            line = lines[i]
            self.getLine(line, i)

    def getLine(self, line, linePosition):
        if "<package>" in line:
            pass

        if "<function>" in line:
            block = []
            params = []

            content = self.toEndBalise("</function>", linePosition)

            for line in content:
                if "<name>" in line:
                    name = self.toEndBalise("</name>")
                    block.append(name, 0)

                if "<summary>" in line:
                    summary = self.toEndBalise("</summary>", linePosition)
                    block.append(summary, 1)

                if "<param>" in line:
                    param = self.toEndBalise("</param>", linePosition)
                    params.append(param)

            block.append(params)
            self.parseXml.append(block)

    def toEndBalise(self, lineFind, linePosition):
        lines = self.file.readLines()
        content = []

        for i in range(linePosition, len(lines)):
            if lineFind in lines[i]:
                return True
            else:
                content.append(lines[i])

    def getParseXml(self):
        return self.parseXml

# All Commande
# <summary>Description</summary>
# <param name="paramName">Description</param>
# 
#
#
#
#
#
#
#
#