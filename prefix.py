from flask import Flask, request, jsonify
app = Flask(__name__)

# Assuming these are the words present in the server
server_words = ['bonfire', 'cardio', 'case', 'character', 'bonsai', 'boot', 'cape', 'candy', 
                'care', 'book', 'bot', 'bank', 'bottle', 'cap', 'cat', 'car', 'cabin', 'cable', 
                'camper', 'camera']

@app.route('/prefixes', methods=['GET'])
def find_prefix():
    keywords = request.args.get('keywords')
    keywords = keywords.split(',')
    output = []

    for keyword in keywords:
        response = {"keyword": keyword}
        if keyword in server_words:
            response["status"] = "found"
            for i in range(1, len(keyword)):
                prefix = keyword[:i]
                if len([w for w in server_words if w.startswith(prefix)]) == 1:
                    response["prefix"] = prefix
                    break
        else:
            response["status"] = "not_found"
            response["prefix"] = "not_applicable"
        output.append(response)
    return jsonify(output)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
