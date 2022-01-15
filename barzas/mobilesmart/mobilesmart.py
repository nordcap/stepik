import re


def insertBarcode(m):
    s1 = m.group("s1")
    s2 = m.group("s2")
    s3 = m.group("s3")

    return "{0}{1}{2} {0}".format(s1, s2, s3) + r'.{CellBarcode:}"'


with open("Cleverence.Warehouse.ProductsBook.xml") as file:
    str_file = file.read()
    out_str = re.sub(r"(?P<s1>barcode=\"\d+)(?P<s2>.*?)(?P<s3><Packings><Packing)", insertBarcode, str_file)
    with open("Cleverence.Warehouse.ProductsBook-new.xml", "w", encoding="utf-8") as out_file:
        out_file.write(out_str)
