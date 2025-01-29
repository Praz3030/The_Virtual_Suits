from flask import Flask, request, jsonify
from flask_cors import CORS
from app.ml_model import predict_answer  # Import your ML function

app = Flask(__name__)
CORS(app)  # Enable cross-origin requests

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        question = data.get("question")

        # Validate input
        if not question:
            return jsonify({"error": "Question is required"}), 400

        # Get prediction from ML model
        answer = predict_answer(question)

        return jsonify({"answer": answer}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(port=8000, debug=True)
