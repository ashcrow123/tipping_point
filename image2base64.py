import base64

def image_to_base64(image_path):

    with open(image_path, "rb") as image_file:
        # 读取图像文件并进行Base64编码
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

def images_to_base64(image_paths):
    encoded_images = []
    for image_path in image_paths:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            encoded_images.append(encoded_string)
    return encoded_images
