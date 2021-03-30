from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)