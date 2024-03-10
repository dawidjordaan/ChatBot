from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot_response():
    user_message = request.json['message']
    return jsonify({"response": "You said: " + user_message})

if __name__ == '__main__':
    app.run(debug=True)