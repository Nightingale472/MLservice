from pydantic import BaseModel

class PredictResponse(BaseModel):
    x_min: float
    y_min: float
    x_max: float
    y_max: float
    class_name: str