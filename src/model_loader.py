import joblib
from src.config import MODEL_PATH, SCALER_PATH


class ModelLoader:
    """
    Loads the trained model and scaler.
    """

    def __init__(self):
        self.model = joblib.load(MODEL_PATH)
        self.scaler = joblib.load(SCALER_PATH)

    def get_model(self):
        return self.model

    def get_scaler(self):
        return self.scaler


loader = ModelLoader()

model = loader.get_model()
scaler = loader.get_scaler()