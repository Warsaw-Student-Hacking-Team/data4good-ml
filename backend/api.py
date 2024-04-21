from fastapi import APIRouter, Depends

from prediction import predict_pm10

api_router = APIRouter()


@api_router.get("/predict_pm10")
def get_ppm10_prediction_route(l_spared: int = 1000):
    prediction = predict_pm10(l_spared)
    return prediction.tolist()
