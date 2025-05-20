# modules/trainer.py

import pandas as pd
import joblib
import os
from sklearn.linear_model import LinearRegression

def train_model_from_csv(csv_path):
    if not os.path.exists(csv_path):
        raise FileNotFoundError("File CSV tidak ditemukan.")

    # Baca dan siapkan data
    df = pd.read_csv(csv_path, parse_dates=['timestamp'])
    df['date'] = df['timestamp'].dt.date
    daily_energy = df.groupby('date')['energy'].sum().reset_index()
    daily_energy.columns = ['date', 'total_energy_kWh']
    daily_energy['day_number'] = range(len(daily_energy))

    # Fitur dan target
    X = daily_energy[['day_number']]
    y = daily_energy['total_energy_kWh']

    # Latih model
    model = LinearRegression()
    model.fit(X, y)

    # Penjelasan model
    explanation = (
        "Model regresi linear telah dilatih dengan data total konsumsi energi harian.\n"
        f"Jumlah data hari: {len(X)}\n"
        f"Koefisien: {model.coef_[0]:.4f}, Intersep: {model.intercept_:.4f}"
    )

    # Bundle untuk disimpan
    model_bundle = {
        'model': model,
        'features': ['day_number']
    }

    return model_bundle, explanation


def save_model(model_bundle, save_path):
    joblib.dump(model_bundle, save_path)
    return f"Model disimpan di: {save_path}"
