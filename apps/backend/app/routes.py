from flask import Blueprint, jsonify

api_routes = Blueprint("api", __name__)

@api_routes.route("/")
def home():
    return "EcoSphere backend running"

@api_routes.route("/health")
def health():
    return jsonify({"status": "ok"})