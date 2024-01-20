from barcode import EAN13,Code128
from barcode.writer import ImageWriter
import qrcode


normor = "200873813009"
product_name = ["fried_chicken_OESHI","tkajf","ajfijri","airx","fried potato"]   

for data in product_name:
    barcode = EAN13(normor,writer=ImageWriter())
    product_barcode = Code128(data,writer=ImageWriter())

    folder_path = "barcode/"

    barcode.save(folder_path+"Barcode")
    product_barcode.save(folder_path+data)


# QR Generate

qr = qrcode.QRCode(
    version=1,  
    error_correction=qrcode.constants.ERROR_CORRECT_L, 
    box_size=10,  
    border=4, 
)

qr.add_data(product_name)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save(folder_path+"qrcode.png")