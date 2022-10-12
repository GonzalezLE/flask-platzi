from typing import Dict

from flask import render_template

from app.forms import LoginForm
from . import auth


@auth.route('/login')
def login():
    login_form = LoginForm()
    
    context:Dict = {
        'login_form':login_form
    }
    
    
    return render_template('login.html',**context) 