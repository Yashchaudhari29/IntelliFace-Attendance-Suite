from PIL import Image
from io import BytesIO
from college_admin.models import *
import requests


img_data = None
api_key = "96nZGD8D9jq_ZaULqKUG21vo1WaSOFkT"
api_secret = "UFF7Q1fyl_RMdCjp6odzEBnRwg_TFIij"
url = "https://api-us.faceplusplus.com/facepp/v3/compare"


def Insert(en_no):
    register.objects.filter(en_no=en_no).update(attended=True)


def Detect_Face(en_no):
    register_entry = register.objects.get(en_no=en_no)

    img_data = register_entry.img.read()
    cap_img_data = register_entry.cap_img.read()
    image_frame = Image.open(BytesIO(cap_img_data))
    image_db = Image.open(BytesIO(img_data))

    image_frame_bytes = BytesIO()
    image_frame.save(image_frame_bytes, format="JPEG")
    image_db_bytes = BytesIO()
    image_db.save(image_db_bytes, format="JPEG")

    data = {
        "api_key": api_key,
        "api_secret": api_secret,
    }

    files = {
        "image_file1": ("image1.jpg", image_frame_bytes.getvalue()),
        "image_file2": ("image2.jpg", image_db_bytes.getvalue()),
    }

    response = requests.post(url, data=data, files=files)

    image_frame.close()
    image_db.close()

    res = response.json()
    if res["confidence"]:

        return res["confidence"]
    else:
        return 0
