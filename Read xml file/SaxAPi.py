import xml.sax


class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        self.CurrentDate = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    def startElementTag(self, tag, attribute):
        self.CurrentDate = tag
        if tag == "movie":
            print("Movie")
            title = attribute['title']
            print("your title is ", title)

    def endElementTag(self, tag):
        if self.CurrentDate == "type":
            print("Type")
        elif self.CurrentDate == "format":
            print("format")
        elif self.CurrentDate == "year":
            print("year")
        elif self.CurrentDate == "rating":
            print("rating")
        elif self.CurrentDate == "stars":
            print("stars")
        elif self.CurrentDate == "description":
            print("Description")

    def characters(self, content):
        if self.CurrentDate == "type":
            self.type = content
        elif self.CurrentDate == "format":
            self.format = content
        elif self.CurrentDate == "year":
            self.year = content
        elif self.CurrentDate == "rating":
            self.rating = content
        elif self.CurrentDate == "stars":
            self.stars = content
        elif self.CurrentDate == "description":
            self.description = content


if (__name__ == "__main__"):
    # create an xml reader
    parser = xml.sax.make_parser()
    # turn of namespace
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    # override the default ContextHandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)
    parser.parse("movies.xml")
