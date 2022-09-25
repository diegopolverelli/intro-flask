# from crypt import methods
from flask import request, abort, render_template
from flask import Flask, url_for, redirect

import mysql.connector

#set FLASK_APP=holamundo.py
#set FLASK_ENV=development


midb=mysql.connector.connect(
    host="localhost",
    user="diego",
    password='Violeta10',
    database='prueba'
)

cursor=midb.cursor(dictionary=True)


app=Flask(__name__)


@app.route('/')
def index():
        return 'hola mundo'


@app.route('/diego/<usuario>')
def prueba_diego(usuario):
        return 'prueba Diego  OK...'+ usuario+'...!!!'


@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def postget(post_id):
    if request.method=='GET':
        return 'el id el post es '+ str(post_id)+'...!!! (via GET, ok)'
    else:
        return 'el id el post es '+ str(post_id)+'...!!! (via POST, ok)'


# @app.route('/post/<int:post_id>', methods=['POST'])
# def postpost(post_id):
#         return 'el id el post es '+ str(post_id)+'...!!!'




@app.route('/prueba', methods=['POST', 'GET'])
def prueba():
    # abort(503) # 401 no autorizado, 403 acceso prohivido... 404 not found, 503 Service Unavailable
    # return redirect(url_for('postget', post_id=109))

    # print(url_for('postget', post_id=109))
    # print(request.form)
    # print(request.form['llave1'])
    # print(request.form['llave2'])

    return render_template('prueba.html')
    # return 'prueba...!!!'

@app.route('/prueba2', methods=['POST', 'GET'])
def prueba2():
    # abort(503) # 401 no autorizado, 403 acceso prohivido... 404 not found, 503 Service Unavailable
    # return redirect(url_for('postget', post_id=109))

    # print(url_for('postget', post_id=109))
    # print(request.form)
    # print(request.form['llave1'])
    # print(request.form['llave2'])

    return {
        "username": "Chanchito Feliz",
        "email": "ch@chancho.com"
    }


@app.route('/home', methods=['POST', 'GET'])
def home():
    cursor.execute('select * from Usuario')
    usuarios=cursor.fetchall()

    return render_template('home.html', mensaje='Hola Mundo...!!!  (desde .py; va al home, y del home carga al bloque content de base.html)', mensaje2='Diego Polverelli (desde .py)',usuarios=usuarios,titulo='Titulo desde .py')


@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method=='POST':
        username=request.form['username']
        email=request.form['email']
        edad=request.form['edad']

        sql='insert into Usuario(username, email, edad) values(%s, %s, %s)'

        values=(username, email, edad)

        cursor.execute(sql, values)
        midb.commit()

        return redirect(url_for('home'))


    return render_template('crear.html')



