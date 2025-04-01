from flask import Flask, request, jsonify

app = Flask(__name__)

CLE_AUTORISEE = "Z51-KEY"

@app.route("/api", methods=["GET"])
def api_access():
    code = request.args.get("key")

    if not code:
        return jsonify({
            "status": "erreur",
            "message": "Mauvaise cle fournie."
        }), 400

    if code == CLE_AUTORISEE:
        return jsonify({
            "status": "autorise",
            "clearance": "TOP-SECRET",
            "message": "Cle acceptee. Connexion etablie.",
            "connexion": "10.31.35.63:8888"
        }), 200

    return jsonify({
        "status": "refuse",
        "message": "Cle incorrecte. Cette tentative a ete enregistree."
    }), 403

@app.route("/api/deep", methods=["GET"])
def deep_access():
    return jsonify({
        "message": "Acces au niveau de profondeur autorise.",
        "param": "MAX_DEPTH = None"
    }), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)
