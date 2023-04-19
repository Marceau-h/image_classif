import json

from imageai.Detection import ObjectDetection
import os
from pathlib import Path

execution_path = os.getcwd()

# detector_path = "modeles/detection/retinanet_resnet50_fpn_coco-eeacb38b.pth"
# detector = ObjectDetection()
# detector.setModelTypeAsRetinaNet()
# detector.setModelPath(detector_path)
# detector.loadModel()


def detect(detector, image_path):
    detections = detector.detectObjectsFromImage(input_image=image_path)

    temp = {}
    for e in detections:
        key = e["name"]
        value = e["percentage_probability"]
        if key not in temp:
            temp[key] = []
        temp[key].append(value)

    return temp


if __name__ == "__main__":

    detectors = [
        (ObjectDetection(), "setModelTypeAsRetinaNet", "retinanet_resnet50_fpn_coco-eeacb38b.pth"),
        (ObjectDetection(), "setModelTypeAsYOLOv3", "yolov3.pt"),
        (ObjectDetection(), "setModelTypeAsTinyYOLOv3", "tiny-yolov3.pt"),
    ]

    for detector, detector_type, detector_path in detectors:
        nom = detector_type.split("As")[1]
        detector.__getattribute__(detector_type)()
        detector.setModelPath(os.path.join(execution_path, "modeles/detection", detector_path))
        detector.loadModel()

        imgs = Path("IMG_Edouard").glob("*/*.jpg")
        dict = {e.as_posix(): detect(detector, e.as_posix()) for e in imgs}

        with open(f"{nom}.json", mode="w", encoding="utf-8") as f:
            json.dump(dict, f, indent=2, ensure_ascii=False)
