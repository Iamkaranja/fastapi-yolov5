import torch
from PIL import Image
import io

def get_yolov5():
    # detected objects whose confidence level > 0.5 will be returned in the result
    model = torch.hub.load('./yolov5', 'custom', path='./model/best.pt', source='local', model=0.5)
    return model

def get_image_from_bytes(binary_image, max_size=1024):
    upload_image=Image.Open(io.BytesIO(binary_image)).convert('RGB')
    width, height = upload_image.size
    resize_factor = min(max_size/width, max_size/height)
    resized_image=upload_image.resize((
        int(width*resize_factor),
        int(height*resize_factor)
        ))
    return resized_image