from cx_Freeze import setup, Executable

executables = [Executable("main.py")]

setup(
    name="Space Invasion",
    version="1.0",
    description="Space Invasion app",
    options={"build_exe": {"packages": ["pygame"]}},
    executables=executables
)
