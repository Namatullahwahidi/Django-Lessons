import xml.sax


class MyHandler(xml.sax.ContentHandler):

    def __init__(self):
        xml.sax.ContentHandler.__init__(self)

    def startElement(self, name, attrs):
        print("Elems=>", name, len(attrs))

    def endElement(self, name):
        print("Element end: =>", name)

    def characters(self, data):
        print("Characters: =>", data)


filename = "movies.xml"
handler = MyHandler()
xml.sax.parse(filename, handler)
