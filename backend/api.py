from fastapi import APIRouter, Depends

from prediction import predict_pm10_day_mean, predict_pm10_hour_mean

api_router = APIRouter()


@api_router.get("/predict_pm10/day")
def get_ppm10_prediction_day_route(l_spared: int = 1000):
    prediction = predict_pm10_day_mean(l_spared)
    return prediction.tolist()


@api_router.get("/predict_pm10/hour")
def get_ppm10_prediction_day_route(l_spared: int = 1000, hour: int = 1):
    prediction = predict_pm10_hour_mean(l_spared, hour)
    return prediction.tolist()
