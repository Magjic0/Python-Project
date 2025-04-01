from flask import Flask, request, jsonify

app = Flask(__name__)

CLE_AUTORISEE = "Z51-KEY"

@app.route("/api", methods=["GET"])
def api_access():
    code = request.args.get("key")

    if not code:
        return jsonify({
            "status": "erreur",
            "message": "Aucune clé fournie."
        }), 400

    if code == CLE_AUTORISEE:
        return jsonify({
            "status": "autorisé",
            "clearance": "TOP-SECRET",
            "message": "Clé acceptée. Connexion établie.",
            "connexion": "192.168.0.42:8888"
        }), 200

    return jsonify({
        "status": "refusé",
        "message": "Clé incorrecte. Cette tentative a été enregistrée."
    }), 403

@app.route("/api/deep", methods=["GET"])
def deep_access():
    return jsonify({
        "message": "Accès au niveau de profondeur autorisé.",
        "param": "MAX_DEPTH = None"
    }), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)
