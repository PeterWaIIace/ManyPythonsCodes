import xml.sax


class Pracownik(xml.sax.ContentHandler):
    def __init__(self):
        self.imie = ""
        self.nazwisko = ""
        self.mail = ""
        self.stanowisko = ""

    def startElement(self,tag,attribute):
        self.CurrentData = tag
        if tag == "pracownik":
            pass


    def characters(self,content):
        if self.CurrentData == "imie":
            self.imie = content
        if self.CurrentData == "nazwisko":
            self.nazwisko = content
        if self.CurrentData == "e-mail":
            self.mail = content
        if self.CurrentData == "stanowisko":
            self.stanowisko = content

    def endElement(self, tag):
        if self.CurrentData == "imie":
            print("Imie:", self.imie)
        elif self.CurrentData == "nazwisko":
            print("Nazwisko:", self.nazwisko)
        elif self.CurrentData == "e-mail":
            print("Mail:", self.mail)
        elif self.CurrentData == "stanowisko":
            print("Stanowisko:", self.stanowisko)
        else:
            pass


def main():
    sax_handler = Pracownik()
    xml.sax.parse("example.xml",sax_handler)
    print(sax_handler.imie)
    file_handler = open('example3.xml','w')
    sax_handler.imie = "test"


if __name__=="__main__":
    main()