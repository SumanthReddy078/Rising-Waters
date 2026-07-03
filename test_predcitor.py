from src.predictor import predict_flood

prediction = predict_flood(
    temp=28,
    humidity=75,
    cloud_cover=40,
    annual=3326.6,
    jan_feb=9.3,
    mar_may=275.7,
    jun_sep=2403.4,
    oct_dec=638.2,
    avgjune=130.3,
    sub=256.4
)

print(prediction)