from flask import Flask, render_template, redirect, url_for, request, flash 
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_usser,current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secrete_key'   #Replace with your secrete key

# Initialise Flask-Login
Login_Manager = LoginManager()
Login_Manager.init_app(app)
Login_Manager.login_view = 'login'   #Redirects unauthorized users to the login page