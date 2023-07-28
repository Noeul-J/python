from flask import Flask, Blueprint, request, render_template, make_response, jsonify, redirect

wb_bp = Blueprint('wb', __name__)

@wb_bp.route('/show_src_result', methods=['POST'])
def show_src_result():
    print('show_src_result', request.form['process_name'], request.form['startDt'], request.form['endDt'])
    return redirect('/wb')


@wb_bp.route('/')
def main_page():
    return render_template('home.html')