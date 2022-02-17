import smtplib
import pandas as pd
from flask import Flask, flash, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jadeubom'

# Carregando data do arquivo


def load_data():
    data = pd.read_excel('lista.xlsx')
    return data

# Envio de email test


def enviar_email(email):
    sender = 'NossoEmail@email.com'
    receivers = [email]

    message = f"""From: From Person <NossoEmail@email.com>
    To: To Person {email}
    Subject: SMTP Teste de email

    Apenas um teste de email.
    """

    smtpObj = smtplib.SMTP('localhost', 1025, 'localhost')
    smtpObj.sendmail(sender, receivers, message)

# Rota das paginas/interface


@app.route('/')
def home():

    return render_template('index.html')

# Envio dos emails da lista.


@app.route('/enviar')
def enviar():
    counter = 0
    try:
        data = load_data()
        for i in data.Email:
            enviar_email(i)
            counter = counter + 1
        flash(f'Foram enviados {counter} emails!')
        flash("""
        Subject: SMTP e-mail test

        This is a test e-mail message.
        """)
    except:
        flash('MSN002 - Sem clientes para envio!')
    return render_template('enviar.html')

# Apresenta lista.


@app.route('/lista')
def lista():
    try:
        data = load_data()
        for i in data.values:
            flash(i)
    except:
        flash('MSN001 - Sem clientes para ser listado!')
    return render_template('lista.html')


if __name__ == '__main__':
    app.run(debug=True)
