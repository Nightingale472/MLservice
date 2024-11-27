import io
from PIL import Image
from ML.load import load_model

model = None

def load_ml():
    global model
    model = load_model()

def save_image(image: bytes, file_name: str):
    img = Image.open(io.BytesIO(image))
    path = f'C://Users/denis/Desktop/savedIMG/{file_name}'
    img.save(path)
    return path


def get_result_from_ml(path):
    results = model.predict(source=path, conf=0.5)
    res = {}
    for r in results:
        boxes = r.boxes.data.tolist()
        for box in boxes:
            res["xmin"] = box[0]
            res["ymin"] = box[1]
            res["xmax"] = box[2]
            res["ymax"] = box[3]
            res["confidence"] = box[4]
            res["class"] = box[5]
            res["class_name"] = model.names[int(box[5])]
    return res
