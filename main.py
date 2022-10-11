
from typing import List,Dict
from flask import Flask,request,make_response,redirect,render_template,session,url_for,flash
from flask_bootstrap import Bootstrap
from settings import settings
from flask_wtf import FlaskForm
from wtforms.fields import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired
app = Flask(__name__)


# Ugly and confusing tangent of in-line config stuff
app.config['TESTING'] = True
app.config['DEBUG'] = True
app.config['FLASK_ENV'] = 'development'
app.config['SECRET_KEY'] = 'GDtfDCFYjD'
# app.config['DEBUG'] = False  # actually I want debug to be off now
bootstrap = Bootstrap(app)

todos : List  = [
    'Comprar cafe',
    'Enviar solicitud de compra',
    'Entregar video a productor'
    ]


class LoginForm(FlaskForm):
    username = StringField('user name' ,validators=[DataRequired()])
    password = PasswordField('Password' ,validators=[DataRequired()])
    submit = SubmitField('Enviar')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html',error=error)


@app.errorhandler(500)
def error_internal_server(error):
    return render_template('500.html',error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    session['user_ip'] =user_ip
    # response.set_cookie('user_ip',user_ip)
    
    return response
    

@app.route('/hello',methods=['GET','POST'])
def hello():
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')
    context:Dict ={
        'user_ip':user_ip,
        'todos':todos,
        'login_form':login_form,
        'username':username
    }
    
    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        
        flash('success register to usser',category = 'success')
        return redirect(url_for('index'))
    
    return render_template('hello.html',**context)





if __name__ == '__main__':
    # app.run(port = 5000, debug = True)
    app.run()