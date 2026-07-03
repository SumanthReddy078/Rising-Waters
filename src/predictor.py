import pandas as pd

from src.model_loader import model


def predict_flood(
    temp,
    humidity,
    cloud_cover,
    annual,
    jan_feb,
    mar_may,
    jun_sep,
    oct_dec,
    avgjune,
    sub
):
    """
    Predict flood occurrence.
    Returns:
        0 -> No Flood
        1 -> Flood
    """

    input_data = pd.DataFrame([{
        "Temp": temp,
        "Humidity": humidity,
        "Cloud Cover": cloud_cover,
        "ANNUAL": annual,
        "Jan-Feb": jan_feb,
        "Mar-May": mar_may,
        "Jun-Sep": jun_sep,
        "Oct-Dec": oct_dec,
        "avgjune": avgjune,
        "sub": sub
    }])

    prediction = model.predict(input_data)

    return int(prediction[0])