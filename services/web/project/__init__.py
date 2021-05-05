from flask import Flask, render_template, Response, request, jsonify, make_response
import json

app = Flask(__name__)

@app.route('/version')
def my_version():
    return jsonify(version='1.0')

@app.route('/health', methods=['GET'])
def health():
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route('/do_something', methods=['GET', 'POST'])
def do_something():
    response = make_response('doing something')
    return response

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)
