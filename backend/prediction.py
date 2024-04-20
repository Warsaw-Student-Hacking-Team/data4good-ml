import onnxruntime as rt
import numpy

MODEL_FILE = "ml_models/PM10_model_v1.onnx"
sess = rt.InferenceSession(MODEL_FILE)

input_name = sess.get_inputs()[0].name
label_name = sess.get_outputs()[0].name


def predict_pm10():
    prediction = {}
    # prediction = sess.run([label_name], {input_name: X_test.astype(numpy.float32)})[0]
    return prediction
