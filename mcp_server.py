from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/mcp', methods=['POST'])
def mcp_handler():
    data = request.get_json()
    
    # For now, just echo back input
    response = {
        "status": "success",
        "message": "MCP server received your request",
        "input_received": data
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
