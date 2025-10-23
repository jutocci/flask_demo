from flask import Flask, render_template, request
import sqlite3

app=Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('meu_banco.db')
    conn.row_factory = sqlite3.Row
    conn.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
                 )
    """)
    conn.commit()
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    usuarios = conn.execute('SELECT * FROM usuarios').fetchall()
    conn.close()
    return render_template('index.html', usuarios=usuarios)


@app.route('/add', methods=('POST',))
def add():
    nome = request.form['nome']
    conn = get_db_connection()
    conn.execute('INSERT INTO usuarios (nome) VALUES (?)', (nome,))
    conn.commit()
    conn.close()
    return 'Usuário adicionado com sucesso! <a href="/">Voltar</a>'

if __name__ == '__main__':
    app.run(debug=True)

