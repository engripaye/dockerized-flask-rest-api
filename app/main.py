from flask import Flask, jsonify, request

app = Flask(__name__)

# in memory data store

todos = []


@app.route('/')
def home():
    return jsonify({"message": "Welcome to the To-Do List API!"}), 200
