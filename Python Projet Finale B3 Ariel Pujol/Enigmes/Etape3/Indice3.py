import os
import sys

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../scripts/flask_api'))
sys.path.insert(0, base_dir)

from app import app

if __name__ == "__main__":
    print("Démarrage de l'API Flask sur http://localhost:5000")
    app.run(debug=True, port=5000)