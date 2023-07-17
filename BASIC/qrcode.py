# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode


# String which represents the QR code
s = "https://www.google.com/maps/place/Sri+Varadevi+Society+Silks/@12.9697638,77.5732196,17z/data=!4m16!1m9!3m8!1s0x3bae160bc0000001:0x9b6784548e669104!2sSri+Varadevi+Society+Silks!8m2!3d12.9697586!4d77.5757945!9m1!1b1!16s%2Fg%2F1w4541jg!3m5!1s0x3bae160bc0000001:0x9b6784548e669104!8m2!3d12.9697586!4d77.5757945!16s%2Fg%2F1w4541jg?entry=ttu"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg file naming "myqr.svg"
url.svg("myqr.svg", scale = 8)

# Create and save the png file naming "myqr.png"
url.png('myqr.png', scale = 6)
