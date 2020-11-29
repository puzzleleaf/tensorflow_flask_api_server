import base64
from . import cartoonize

def convert(image):
    model_path = './v1/image/cartoongan/saved_models'
    imgdata = base64.b64decode(image)
    cartoon_img_data = cartoonize.cartoonize(imgdata, model_path)

    return base64.b64encode(cartoon_img_data)