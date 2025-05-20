import pandas as pd

# Baca file CSV
df = pd.read_csv("data_listrik_rumah_tangga.csv", parse_dates=['timestamp'])

# Tampilkan 5 data teratas
print(df.head())

# Info data
print(df.info())

# === Agregasi Energi Harian ===

# Tambahkan kolom tanggal saja (tanpa jam)
df['date'] = df['timestamp'].dt.date

# Hitung total energi per hari
daily_energy = df.groupby('date')['energy'].sum().reset_index()
daily_energy.columns = ['date', 'total_energy_kWh']

# Tampilkan hasil agregasi harian
print(daily_energy.head())
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

# Buat fitur hari ke-n
daily_energy['day_number'] = range(len(daily_energy))

# Siapkan fitur dan target
X = daily_energy[['day_number']]     # Fitur: hari ke-n
y = daily_energy['total_energy_kWh'] # Target: konsumsi listrik

# Bagi data menjadi training dan testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Buat dan latih model Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluasi model
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"\nMean Absolute Error (MAE): {mae:.4f} kWh")

# Prediksi konsumsi listrik pada hari ke-61 (next day)
future_day = [[len(daily_energy)]]
predicted_energy = model.predict(future_day)
print(f"Prediksi konsumsi listrik hari ke-{len(daily_energy)+1}: {predicted_energy[0]:.2f} kWh")

# Visualisasi
plt.figure(figsize=(10, 5))
plt.scatter(X, y, label='Data Asli')
plt.plot(X, model.predict(X), color='red', label='Regresi Linear')
plt.xlabel('Hari ke-n')
plt.ylabel('Total Energi (kWh)')
plt.title('Prediksi Konsumsi Listrik Harian')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
