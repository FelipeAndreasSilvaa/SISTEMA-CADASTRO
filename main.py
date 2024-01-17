import mysql.connector
from flask import Flask, render_template, url_for, request, flash, redirect

app = Flask(__name__)
app.secret_key = "flash_message"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Ciclope10$'
app.config['MYSQL_DB'] = 'sistema_login_cadastro'

mysql_conn = mysql.connector.connect(
    host = app.config['MYSQL_HOST'],
    user = app.config['MYSQL_USER'],
    password = app.config['MYSQL_PASSWORD'],
    db = app.config['MYSQL_DB']
)

@app.route('/', methods = ['POST', 'GET'])
def login():
    message = None
    
    if request.method == "POST":
        email = request.form['email']
        senha = request.form['senha']
        
        # verifica campos
        if not email or not senha:
            message = "Por favor, insira os dados corretamnete"
        else:  
            cursor = mysql_conn.cursor()
            query = "SELECT * FROM usuarios WHERE email = %s AND senha = %s"
            cursor.execute(query, ( email, senha))
            user = cursor.fetchone()
            
            if user:
                flash("Login realizado com sucesso")
                nome_user = user[1]
                return redirect(url_for('home', nome=nome_user))
            else:
                message = "Dados invalidos. Tente novamente"
    return render_template('login.html', message=message)

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/home/<nome>')
def home(nome):
    return render_template('home.html', nome = nome)

@app.route('/insert', methods = ['POST'])
def insert():
    flash("Cadastro realizado com sucesso!")
    if request.method == "POST":
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        
        cursor = mysql_conn.cursor()
        query = 'INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)'
        cursor.execute(query, (nome, email, senha))
        mysql_conn.commit()
        return redirect(url_for('home', nome=nome))

if __name__ == "__main__":
    app.run(debug=True)
