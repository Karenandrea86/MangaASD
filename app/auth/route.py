from app.auth import auth
from flask import Flask, render_template, redirect, flash
import app
from .forms import LoginForm
from flask_login import login_user, current_user, logout_user

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')
