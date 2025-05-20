@echo off
REM Aktifkan virtual environment
call my_venv\Scripts\activate.bat

REM Jalankan script Python
python main.py

REM Pause agar jendela terminal tidak langsung tertutup
pause
