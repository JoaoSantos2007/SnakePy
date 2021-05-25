import sys
import cx_Freeze


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("Snake.py", base=base,icon="snake.ico")
]

buildOptions = dict(
        packages = [],
        includes = [],
        include_files = [],
        excludes = []
)




setup(
    name = "Jogo da Cobrinha",
    version = "2.0",
    description = "Jogo da cobrinha em python",
    options = dict(build_deb = buildOptions),
    executables = executables
 )
