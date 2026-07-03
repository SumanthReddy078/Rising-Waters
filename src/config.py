from pathlib import Path

# Project Root Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Models Directory
MODELS_DIR = BASE_DIR / "models"

# Saved Model Path
MODEL_PATH = MODELS_DIR / "floods.save"

# Saved Scaler Path
SCALER_PATH = MODELS_DIR / "scaler.pkl"