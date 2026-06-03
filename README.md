# bad*ss launcher
a launcher for freedoom bad*ss edition
## dependencies
- [python](https://www.python.org/downloads/)
- [git](https://git-scm.com/install/)
- tkinter (it usually comes with python but in some instances it doesn't)
	- if you're on linux you can write `sudo apt install python3-tk` into the terminal to install it
- [GitPython](https://gitpython.readthedocs.io/en/stable/intro.html) ([PyPI](https://pypi.org/project/GitPython/))
- [configparser](https://pypi.org/project/configparser/)
- [Pillow](https://pypi.org/project/pillow/)
- [pyinstaller](https://pypi.org/project/pyinstaller/) (optional, required for packaging the app)
## setup
ensure that all dependencies are installed then write `python3 src/main.py` into the terminal when you're in the repo's directory to run the app

if you want to package the app into an executable you can write `pyinstaller src/main.py --hidden-import='PIL._tkinter_finder'` into the terminal
when it's done packaging copy the assets directory to dist/main and launch main(.exe if you're on windows)

