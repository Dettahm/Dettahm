# --- main.py ---
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from modules import data_loader, trainer, evaluator
import os

class ElectricityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard AI Konsumsi Listrik")
        self.root.geometry("1200x700")

        self.csv_path = None
        self.model_path = None

        self.create_menu()
        self.create_canvas()

    def create_menu(self):
        menu_frame = tk.Frame(self.root, bg='#e8e8e8', width=200)
        menu_frame.pack(side=tk.LEFT, fill=tk.Y)

        tk.Label(menu_frame, text="Menu", font=('Helvetica', 16, 'bold'), bg='#e8e8e8').pack(pady=20)

        tk.Button(menu_frame, text="Get Data", command=self.get_data, width=20).pack(pady=10)
        tk.Button(menu_frame, text="Train Model", command=self.train_model, width=20).pack(pady=10)
        tk.Button(menu_frame, text="Evaluasi Model", command=self.evaluate_model, width=20).pack(pady=10)
        tk.Button(menu_frame, text="Exit", command=self.root.quit, width=20).pack(pady=10)

    def create_canvas(self):
        self.plot_frame = tk.Frame(self.root)
        self.plot_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def get_data(self):
        self.csv_path = filedialog.askopenfilename(title="Pilih file CSV", filetypes=[("CSV files", "*.csv")])
        if self.csv_path:
            fig = data_loader.plot_data_from_csv(self.csv_path)
            self.show_plot(fig)

    def train_model(self):
        if not self.csv_path:
            messagebox.showwarning("Peringatan", "Silakan pilih data CSV terlebih dahulu.")
            return

        model, explanation = trainer.train_model_from_csv(self.csv_path)

        # Prompt untuk menyimpan file model
        file_path = filedialog.asksaveasfilename(defaultextension=".pkl", filetypes=[("Pickle files", "*.pkl")],
                                                 title="Simpan model sebagai")
        if file_path:
            trainer.save_model(model, file_path)
            explanation += f"\nModel disimpan di: {file_path}"
        else:
            explanation += "\nModel tidak disimpan karena pengguna membatalkan."

        messagebox.showinfo("Model Disimpan", explanation)

    def evaluate_model(self):
        if not self.csv_path:
            messagebox.showwarning("Peringatan", "Silakan pilih data CSV terlebih dahulu.")
            return

        self.model_path = filedialog.askopenfilename(title="Pilih file model .pkl", filetypes=[("Pickle files", "*.pkl")])
        if not self.model_path:
            return

        fig, explanation = evaluator.evaluate_model_from_csv(self.csv_path, self.model_path)
        messagebox.showinfo("Evaluasi Model", explanation)
        self.show_plot(fig)

    def show_plot(self, fig):
        for widget in self.plot_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

if __name__ == '__main__':
    root = tk.Tk()
    app = ElectricityApp(root)
    root.mainloop()
