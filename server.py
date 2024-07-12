from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"

my_message = {
    'message': 'Hi there!',
    'message2': 'Yellow!'
}

@app.route('/get', methods=['GET'])
def get_message():
    return jsonify(my_message)

@app.route('/post', methods=['POST'])
def post_message():
    data = request.get_json()
    message = data.get('message', 'Say Hi to Isha!')
    return jsonify({'response': f'You sent: {message}'})

@app.route('/put', methods=['PUT'])
def put_message():
    retrieve_data = request.get_json()
    if 'message' in retrieve_data:
        my_message['message'] = retrieve_data['message']
        return jsonify({'response': 'Yayy! Updated!'})
    else:
        return jsonify({'error': 'Oops! No message has been provided!'}), 400

@app.route('/delete', methods=['DELETE'])
def delete_message():
    global my_message
    if 'message2' in my_message:
        del my_message['message2']
        return jsonify({'response': 'Yayy! Message deleted!'})
    else:
        return jsonify({'error': 'There is no message to delete!'}), 404


if (__name__ == '__main__'):
    app.run(host='0.0.0.0')

