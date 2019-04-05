from app import app
from flask import Flask, request, redirect, url_for, render_template, make_response
import smtplib, ssl
from flask_mail import Mail, Message
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mail', methods=['POST','GET'])
def send_mail():
    if request.method == 'POST':
        bairro = request.form['bairro']
        email = request.form['email']
        nome = request.form['nome']
        telefone = request.form['telefone']
        message = bairro+'    '+email+'    '+nome+'    '+telefone
        sender_email = "gavsaude@gmail.com"
        password = "" #input your password here
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo() #Identify computer
        mail.starttls()
        mail.login(sender_email, password)
        header = 'To:'+sender_email+'\n'+'Subject:'+nome+'\n'
        message = header+message
        mail.sendmail('gavsaude@gmail.com','gavsaude@gmail.com',message)

        return make_response(render_template('index.html'), 200) #Force 200