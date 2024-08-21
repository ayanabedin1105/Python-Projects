import qrcode
from qrcode import QRCode
qr = QRCode(version=1, box_size=10, border=5, error_correction = qrcode.constants.ERROR_CORRECT_H)

# Define the data to be encoded in the QR code
data = "https://medium.com/@rahulmallah785671/create-qr-code-by-using-python-2370d7bd9b8d#:~:text=To%20create%20a%20QR%20code,a%20text%20or%20a%20URL."

# add the data to the QR code object
qr.add_data(data)

# make the QR Code
qr.make(fit=True)

# create an image from the QR Code with a black fill color and white background
img = qr.make_image(fill_color = "black", back_color="white")

# save the QR code image
img.save("qr_code.png")