from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Mistral AI API kalitini o'rnatish
MISTRAL_API_KEY = "zDqFt9U0Dv2boeIfj57IaR7x5jLVC7Ab"
API_URL = "https://api.mistral.ai/v1/chat/completions"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_input = request.json.get("message")

        headers = {
            "Authorization": f"Bearer {MISTRAL_API_KEY}",
            "Content-Type": "application/json"
        }
    
        data = {
            "model": "mistral-medium",
            "messages": [
                {"role": "system", "content": "Sen aqlli sun'iy intellektsan va faqat o'zbek tilda javob berasan."},
                {"role": "user", "content": user_input}
            ]
        }

        response = requests.post(API_URL, json=data, headers=headers)
        response_json = response.json()

        # Mistral javobini chiqarish
        ai_reply = response_json["choices"][0]["message"]["content"]

        return jsonify({"response": ai_reply})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
