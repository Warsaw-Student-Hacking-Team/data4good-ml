import numpy as np
from onnxruntime import InferenceSession

from sample_data import example_traffic_values

MODEL_FILE = "ml_models/PM10_model_v1.onnx"


def predict_pm10_internal(l_spared, traffic_values, month, hour):
    traffic_values = np.array(traffic_values, dtype=np.float32)
    month = np.array([month], dtype=np.float32)
    hour = np.array([hour], dtype=np.float32)
    onnx_session = InferenceSession(MODEL_FILE)

    num_of_traffic_stations = len(traffic_values) // 2
    k = 10

    real_input = np.concatenate([traffic_values, month, hour])

    traffic_values[:num_of_traffic_stations] += k * l_spared / 24 / num_of_traffic_stations

    input_without_our_app = np.concatenate([traffic_values, month, hour])

    real_traffic_estimates = onnx_session.run([], {'input_0': real_input.reshape(1, real_input.shape[0])})
    without_app_traffic_estimates = onnx_session.run([],
                                                     {'input_0': input_without_our_app.reshape(1, real_input.shape[0])})

    average_traffic_est_real = np.mean(real_traffic_estimates)
    average_traffic_est_without_app = np.mean(without_app_traffic_estimates)

    return average_traffic_est_real, average_traffic_est_without_app


def predict_pm10_day_mean(l_spared):
    l1, l2 = [], []
    month = 1

    for i, hour in enumerate(range(24)):
        real_traffic_estimates, without_app_estimates = predict_pm10_internal(
            l_spared,
            example_traffic_values[i],
            month,
            hour
        )
        l1.append(real_traffic_estimates)
        l2.append(without_app_estimates)

    return np.mean(np.array(l2) - np.array(l1))


def predict_pm10_hour_mean(l_spared, hour):
    l1, l2 = [], []
    month = 1

    real_traffic_estimates, without_app_estimates = predict_pm10_internal(
        l_spared,
        example_traffic_values[hour],
        month,
        hour
    )
    l1.append(real_traffic_estimates)
    l2.append(without_app_estimates)

    return np.mean(np.array(l2) - np.array(l1))
