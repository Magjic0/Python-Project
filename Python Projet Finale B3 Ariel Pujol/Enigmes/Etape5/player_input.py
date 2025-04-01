import os
import sys
import subprocess

#Paramètre à modifier 
N_ESTIMATORS = ""
MAX_DEPTH = ""



script_dir = os.path.dirname(os.path.abspath(__file__))
ml_engine_path = os.path.abspath(os.path.join(script_dir, "..", "..", "scripts", "ml", "ml_engine.py"))

command = f'"{sys.executable}" "{ml_engine_path}" {N_ESTIMATORS} {MAX_DEPTH}'
subprocess.run(command, shell=True)



