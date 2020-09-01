@echo off
SET PATH=C:\Compilers\Python37\Scripts\;C:\Compilers\Python37\;%PATH%
python -m venv .venv
call .venv\Scripts\activate.bat
pip install -r requirements.txt