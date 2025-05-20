import joblib

def predict_future_energy(model_path, current_day_number):
    model = joblib.load(model_path)
    future_day = [[current_day_number + 1]]
    prediction = model.predict(future_day)
    return prediction[0]
