import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def evaluate_model_from_csv(csv_path, model_path):
    # Load model
    loaded = joblib.load(model_path)
    
    # Handle jika model disimpan sebagai dict (dengan fitur)
    if isinstance(loaded, dict):
        model = loaded.get('model')
        feature_columns = loaded.get('features', ['day_number'])
    else:
        model = loaded
        feature_columns = ['day_number']  # default asumsi

    # Load data
    df = pd.read_csv(csv_path, parse_dates=['timestamp'])
    df['date'] = df['timestamp'].dt.date
    daily_energy = df.groupby('date')['energy'].sum().reset_index()
    daily_energy.columns = ['date', 'total_energy_kWh']
    daily_energy['day_number'] = range(len(daily_energy))

    # Prediksi
    X = daily_energy[feature_columns]
    y = daily_energy['total_energy_kWh']
    y_pred = model.predict(X)

    # Hitung metrik evaluasi
    mae = mean_absolute_error(y, y_pred)
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)
    mean_actual = y.mean()
    mae_percent = (mae / mean_actual) * 100
    accuracy = 100 - mae_percent

    # Plot
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(daily_energy['date'], y, label='Aktual', marker='o')
    ax.plot(daily_energy['date'], y_pred, label='Prediksi', marker='x')
    ax.set_title("Prediksi vs Aktual Konsumsi Energi Harian")
    ax.set_xlabel("Tanggal")
    ax.set_ylabel("Total Energi (kWh)")
    ax.legend()
    ax.grid(True)
    fig.tight_layout()

    # Penjelasan naratif
    explanation = (
    f"Mean Absolute Error (MAE): {mae:.4f} kWh\n"
    f"MAE (% dari rata-rata aktual): {mae_percent:.2f}%\n"
    f"Akurasi Perkiraan (approx.): {accuracy:.2f}%\n"
    f"R-squared (R²): {r2:.4f}\n\n"
    f"Model ini menunjukkan bahwa rata-rata selisih antara prediksi dan data aktual adalah {mae:.4f} kWh.\n"
    f"Semakin kecil MAE, semakin akurat model.\n"
    f"Nilai R² sebesar {r2:.4f} menunjukkan seberapa baik model menjelaskan variasi dalam konsumsi energi.\n"
    f"Semakin mendekati 1, semakin baik kecocokan model.\n"
    f"Grafik menunjukkan seberapa baik prediksi mengikuti data aktual."
)


    return fig, explanation
