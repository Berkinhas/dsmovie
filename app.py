from flask import Flask, request, render_template, url_for, redirect
app = Flask(__name__)

@app.route('/<string:nome>')
def error(nome):
    return f'<h1>A página ({nome}) não existe!</h1>'

@app.route('/')
def index():  
    return render_template('index.html')

@app.route('/registro')
def registro():  
    return render_template('registro.html')

@app.route('/home')
def home():  
    return render_template('home.html')



app.run(debug=True)