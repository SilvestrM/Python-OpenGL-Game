import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
additional_modules = []

build_exe_options = {"includes": additional_modules,
                     "packages": ["OpenGL", "sys", "os", "pyglet",
                                  "src/display", "src/game_objects", "src/levels", "src/main",
                                  "src/model", "src/utils"],
                     "excludes": ['tkinter'],
                     'include_msvcr': True
                     # "include_files": ['icon.ico', 'res']
                     }

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="PGRF Game",
      version="1.0",
      description="OpenGL project",
      options={"build_exe": build_exe_options},
      executables=[Executable(script="src/app.py", base=base)])
