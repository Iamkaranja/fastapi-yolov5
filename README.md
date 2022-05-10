# yolov5-fastapi
A machine learning model API using YOLOv5 and FastAPI

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
