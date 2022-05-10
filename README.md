# yolov5-fastapi
This machine learning application model will perform object detections by allowing a user to upload images and get back results in JSON or image format.

## Repo Breakdown
```sh
.
├── Dockerfile # For containerization of this application
├── README.md
├── main.py # The entry point of the program
├── model/ # The model files
│   └── best.pt # The trained custom model generated from YOLOv5
├── requirements.in # To generate requirements.txt
├── requirements.txt # Usage: pip install -r requirements.txt
├── segmentation.py # importing local YOLOv5 and scale image
└── yolov5 # YOLOv5 repo from https://github.com/ultralytics/yolov5
```
### Prerequisites
Install the packages required for this project
```sh
pip install -r requirements.txt
```

### Teck Stack

* Tech-stack
    * [FastAPI](https://fastapi.tiangolo.com/) - Fast API framework for serving authentication API with the asynchronous pattern.
    * [YOLOv5](https://github.com/ultralytics/yolov5) - For training custom object detection models
    * [Docker](https://www.docker.com/) -Building container images.

## To start for this project
```sh
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## To build the docker image
```sh
docker build -t yolov5-fastapi .
```

## To run the docker container of the image
```sh
docker run -it --rm -p 8000:8000 yolov5-fastapi
```

The application will be available on http://localhost:8000/


Todo:
* [x] Add dockerfile
* [] Add authentication to the api
* [] Add feature: store detected result into a database
* [] Add more tests

