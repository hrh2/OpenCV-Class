import pyzxing

reader = pyzxing.BarCodeReader()

barcode = reader.decode('../data/IMG_2019.jpg')

if barcode:
    print("Decoded Data:", barcode[0]['raw'])
else:
    print("No Data Matrix code found.")