from flask import Flask, render_template, redirect, request
import pandas

app = Flask(__name__)


@app.route('/admin', methods=['GET'])
def adminPage():
    return 'ho'
