import pandas as pd
import matplotlib.pyplot as plt

def plot_data_from_csv(csv_path):
    df = pd.read_csv(csv_path, parse_dates=['timestamp'])

    if 'energy' not in df.columns:
        raise ValueError("File CSV tidak memiliki kolom 'energy'.")

    # Cek apakah timestamp mengandung jam
    if df['timestamp'].dt.hour.max() > 0:
        df['date'] = df['timestamp'].dt.date
        daily_energy = df.groupby('date')['energy'].sum().reset_index()
    else:
        daily_energy = df.copy()
        daily_energy['date'] = pd.to_datetime(daily_energy['timestamp']).dt.date
        daily_energy = daily_energy[['date', 'energy']]

    # Plot
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(daily_energy['date'], daily_energy['energy'], marker='o', linestyle='-')
    ax.set_title('Visualisasi Konsumsi Energi Harian')
    ax.set_xlabel('Tanggal')
    ax.set_ylabel('Energi (kWh)')
    ax.grid(True)

    return fig
