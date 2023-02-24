
from PIL import Image
import base64
from io import BytesIO


def base64ToImage(base64String):
    imgdata = base64String

    bytes_decoded = base64.b64decode(imgdata)

    img = Image.open(BytesIO(bytes_decoded))

    # # to jpg
    out_jpg = img.convert("RGB")

    # save file
    out_jpg.save("saved_img.jpg")

    return "saved_img.jpg"
