from fastapi import APIRouter, Depends

from prediction import predict_pm10

api_router = APIRouter()


@api_router.get("/predict_pm10")
def get_ppm10_prediction_route():
    return predict_pm10()
