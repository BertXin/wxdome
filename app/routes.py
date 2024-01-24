# app/routes.py
from app import app
from flask import render_template, request, redirect, url_for

# 用于登录验证的硬编码凭据（在实际应用中应该使用数据库）
USER_CREDENTIALS = {'username': 'user', 'password': 'pass'}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
        return redirect(url_for('welcome'))
    return redirect(url_for('index'))

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')
