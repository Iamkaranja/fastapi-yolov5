from fastapi import FastAPI, File
from segmentation import get_yolov5, get_image_from_bytes
import io
from starlette.responses import Response
from PIL import Image
import json
from fastapi.middleware.cors import CORSMiddleware

model = get_yolov5()

app = FastAPI(
    title='Custom YOLOv5 Machine Learning',
    description="""obtain object value out of an image and return image, json result""", 
    version='0.0.2'
    )

origins= ["http://localhost","http://localhost:8080", "*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

# path: /status/v1/health
@app.get('/status/v1/health')
def check_health():
    return dict(msg='OK')

# path: /v1/predict/object-to-json
@app.post('/v1/predict/object-to-json')
async def detect_object_return_json_result(file: bytes = File(...)):
    upload_image=get_image_from_bytes(file)
    result=model(upload_image)
    detect_res = result.pandas().xyxy[0].to_json(orient="records")
    detect_res = json.loads(detect_res)
    return {"result": detect_res}

#  path: /v1/predict/object-to-image
@app.post('/v1/predict/object-to-image')
async def food_return_base64_img(file: bytes = File(...)):
    upload_image=get_image_from_bytes(file)
    results = model(upload_image)
    # updates resuts.imgs with boxes and labels
    results.render()
    for img in results.imgs:
        bytes_io = io.BytesIO()
        img_base64 = Image.fromarray(img)
        img.save(bytes_io, format='jpeg')
    return Response(content=bytes_io.getvalue(), media_type='image/jpeg')