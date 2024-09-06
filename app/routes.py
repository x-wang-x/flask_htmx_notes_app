from flask import render_template, request, redirect, url_for, make_response
from app import app
from app.models import *
import time

@app.route('/')
def index():
    notes = get_all_notes();
    response = make_response(render_template('index.html', notes=notes))
    return response

@app.route('/wait')
def wait():
    time.sleep(5)
    return f'COK'

@app.route('/add_note', methods=['POST'])
def add_note():
    response = make_response()
    response.status_code = 200
    response.headers['HX-Trigger'] = 'load-data'
    content = request.form['content']
    if content.strip():
        add_notes(content)
    return response;

@app.route('/delete_note/<int:id>',methods=['DELETE'])
def delete_note(id):
    response = make_response()
    response.status_code = 200
    response.headers['HX-Trigger'] = 'load-data'
    result = delete_notes(id)
    if not result:
        return "Failed",400
    return response

@app.route('/show_all',methods=['GET'])
def show_all():
    if request.method != "GET" :
        return "Failed",405
    notes = get_all_notes();
    if notes:
        return render_template('show_all.html',notes=notes)
    return "<li> No Result </li>"