
from typing import List,Dict
from flask import (
    request,
    make_response,
    redirect,
    render_template,
    session,
    url_for,flash
    )


from app import create_app
from app.forms import LoginForm

app = create_app()

todos : List  = [
    'Comprar cafe',
    'Enviar solicitud de compra',
    'Entregar video a productor'
    ]





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
    

@app.route('/hello',methods=['GET'])
def hello():
    user_ip = session.get('user_ip')
    
    username = session.get('username')
    context:Dict ={
        'user_ip':user_ip,
        'todos':todos,        
        'username':username
    }
    
    return render_template('hello.html',**context)





if __name__ == '__main__':
    # app.run(port = 5000, debug = True)
    app.run()