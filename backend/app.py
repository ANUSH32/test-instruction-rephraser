from flask import Flask, request, jsonify
from flask_cors import CORS
import cohere

app = Flask(__name__)
CORS(app)

co = cohere.Client("jrAZICzKn4DXxr3EU4P3aTR4JVO8EqpkLhhQEzWB")

@app.route('/api/rephrase', methods=['POST'])
def rephrase():
    data = request.get_json()
    if not data or 'input' not in data:
        return jsonify({"error": "Missing 'input' in request body"}), 400
    user_input = data['input']
    prompt = f"Rephrase the following into a clear, testable instruction: {user_input}"
    try:
        response = co.generate(model='command-r-plus', prompt=prompt, max_tokens=100)
        rephrased_text = response.generations[0].text.strip()
        return jsonify({"rephrased": rephrased_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
