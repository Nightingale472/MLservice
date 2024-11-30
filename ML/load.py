from ultralytics import YOLO

def load_model():
    model = YOLO("best.pt")
    model.eval()
    return model

model = load_model()
