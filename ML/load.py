from ultralytics import YOLO

def load_model():
    model = YOLO("C://Users/denis/PycharmProjects/pythonProject1/ML/best.pt")
    model.eval()
    return model

model = load_model()

#results = model.predict(source="C://Users/denis/Downloads/1.jpg", conf=0.5)

# res = {}
#
# for r in results:
#     boxes = r.boxes.data.tolist()
#     for box in boxes:
#         res["xmin"] = box[0]
#         res["ymin"] = box[1]
#         res["xmax"] = box[2]
#         res["ymax"] = box[3]
#         res["confidence"] = box[4]
#         res["class"] = box[5]
#         res["class_name"] = model.names[int(box[5])]

#print(res)