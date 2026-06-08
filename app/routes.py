from flask import jsonify, render_template, abort

from app.database import MALWARE_DATABASE


def register_routes(app):

    @app.route("/")
    def index():
        samples = list(MALWARE_DATABASE.values())
        return render_template("index.html", samples=samples)

    @app.route("/malware/<id>")
    def malware_detail(id):
        sample = MALWARE_DATABASE.get(id)
        if sample is None:
            abort(404)
        return render_template("malware.html", sample=sample)

    @app.route("/api/v1/malware/<id>")
    def api_malware(id):
        sample = MALWARE_DATABASE.get(id)
        if sample is None:
            abort(404)
        return jsonify(sample)
