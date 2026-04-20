#install pre-installments
pip install Ultralytics

#import the YOLO from ultralytics
from ultralytics import YOLO
model = "yolov8l.pt"
data = "dataset yaml file location"
epochs = 100
imgsz = 640

yolo = YOLO()

#train the model
yolo.train(
 task="detect",
 mode="train",
 model=model,
 data=data,
 epochs=epochs,
 imgsz=imgsz,
)
