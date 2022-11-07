import xml.sax
import xml.dom.minidom
import csv
import sys

class SAX_CDHandler(xml.sax.ContentHandler):

    def __init__(self):
        self.current = ""
        self.title = ""
        self.artist = ""
        self.country = ""
        self.company = ""
        self.price = ""
        self.year = ""

    def startElement(self, name, attrs):
        self.current = name
        if name == "cd":
            print(f"CD id: {attrs['id']}")

    def characters(self, attrs):
        if self.current == "title":
            self.title = attrs
        elif self.current == "artist":
            self.artist = attrs
        elif self.current == "country":
            self.country = attrs
        elif self.current == "company":
            self.company = attrs
        elif self.current == "price":
            self.price = attrs
        elif self.current == "year":
            self.year = attrs


    def endElement(self, attrs):
        if self.current == "title":
            print(f"Title: {self.title}")
        elif self.current == "artist":
            print(f"Artist: {self.artist}")
        elif self.current == "country":
            print(f"Country: {self.country}")
        elif self.current == "company":
            print(f"Company: {self.company}")
        elif self.current == "price":
            print(f"Price: {self.price}")
        elif self.current == "year":
            print(f"Year: {self.year}")
        self.current = ""

def main_parser():
    # SAX parser
    parser = xml.sax.make_parser()
    xml_handler = SAX_CDHandler()
    parser.setContentHandler(xml_handler)
    parser.parse("xmlsample.xml")

    # DOM parser
    xml_dom_handler = xml.dom.minidom.parse("xmlsample.xml")
    cds = xml_dom_handler.documentElement.getElementsByTagName('cd')

    cd_title = cds[0].getElementsByTagName('title')[0].childNodes[0].data
    cd_price = cds[0].getElementsByTagName('price')[0].childNodes[0].data

    # change
    cds[0].getElementsByTagName('title')[0].childNodes[0].data = 'hehe'
    with open('xmlsample_domi_changed.xml', 'w+') as new_file:
        new_file.write(xml_dom_handler.toxml())


class CsvFileManager:

    def __init__(self, path):
        self.path = path

    def ShowData(self):

        with open(self.path, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)

            for record_index, line in enumerate(reader):
                print(f"Record index: {record_index + 1}")
                for index_field, header_field in enumerate(header):
                    print(f"{header_field} - {line[index_field]}")
                print()

    def AddNewData(self):

        with open(self.path, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)

        new_data = [input(f"Enter {header_field}: ") for header_field in header]

        with open(self.path, 'a+', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_data)

    def DeleteData(self):

        record = int(input("Enter the number of record to delete: "))

        if record == 0:
            print("Invalid number of record")
            return

        with open(self.path, 'r') as file:
            reader = csv.reader(file)
            lines = [row for row in reader]

            for index, line in enumerate(lines):
                if record == index:
                    lines.remove(line)
                    break
            else:
                print("Invalid number of record")
                return

        with open(self.path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(lines)

    def Menu(self):

        menu = {
            1: self.ShowData,
            2: self.AddNewData,
            3: self.DeleteData,
            4: sys.exit
        }

        while True:
            select = int(input("Csv File Manager\n1 - Show data\n2 - Add new data\n3 - Delete record\n4 - Exit program\n"))
            try:
                menu[select]()
            except KeyError:
                print("Wrong input")


if __name__ == '__main__':

    main_parser()
    print("\n\n\n")
    handler = CsvFileManager("deniro.csv")
    handler.Menu()



