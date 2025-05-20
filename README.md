# 🔌 Prediksi Konsumsi Energi Listrik Rumah Tangga

Proyek ini bertujuan untuk memprediksi konsumsi energi listrik harian berbasis data dari sensor PZEM-004T. Dengan menggunakan algoritma Machine Learning Linear Regression, pengguna dapat:
- Memvisualisasikan data konsumsi energi harian
- Melatih model regresi dari data CSV
- Menyimpan dan mengevaluasi model
- Melihat grafik prediksi vs aktual

---

## 📁 Struktur Folder
>main.py # Antarmuka utama aplikasi berbasis Tkinter
data_loader.py # Modul untuk memuat dan memvisualisasi data
trainer.py # Modul untuk melatih dan menyimpan model
evaluator.py # Modul untuk mengevaluasi model dan visualisasi
predictor.py # (opsional) Untuk prediksi masa depan
/Modules # Folder tempat modul disimpan
/Models # Folder menyimpan model hasil training (.pkl)
/Data Dummy # Folder menyimpan contoh CSV
README.md # Dokumentasi proyek
.gitignore # File ignore untuk Git


---

## 🚀 Cara Menjalankan
1. **Instal virtual environment (opsional):**
   ```bash
   python -m venv my_venv
   .\my_venv\Scripts\activate
2.Install dependensi:
    pip install -r requirements.txt
3.Jalankan aplikasi:
    python main.py

🧠 Algoritma yang Digunakan
Linear Regression (Scikit-Learn)
Model ini digunakan untuk memprediksi konsumsi energi berdasarkan jumlah hari (day_number).

📊 Evaluasi Model
Model akan menampilkan metrik evaluasi:

MAE (Mean Absolute Error)

MAE dalam persen

R² (koefisien determinasi)

Visualisasi grafik aktual vs prediksi

🧰 Dependensi Utama
Python ≥ 3.10

Tkinter

Matplotlib

Pandas

scikit-learn

joblib

📬 Kontak
Dibuat oleh Deta Hata Maulana
Email: Deta.122490003@student.itera.ac.id
Email: detahatamaulana@gmail.com
Repo: https://github.com/Dettahm/Dettahm
