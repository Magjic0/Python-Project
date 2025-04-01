import webbrowser
import os
import pathlib

relative_path = os.path.join("scripts", "scraping", "indice_zone51.html")
abs_path = pathlib.Path(relative_path).resolve()

webbrowser.open(f"file://{abs_path}")
