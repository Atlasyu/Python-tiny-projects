from cx_Freeze import setup, Executable
import sys
import os
os.environ['TCL_LIBRARY'] = "C:\\Anaconda3\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Anaconda3\\tcl\\tk8.6"

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"


setup(name='Database',version='0.1',description='Bookstore',executables = [Executable('frontend.py')])
