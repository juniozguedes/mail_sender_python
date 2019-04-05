from flask import Flask, request, redirect, url_for, render_template
from flask_modus import Modus
import smtplib, ssl
from flask_mail import Mail, Message

app = Flask(__name__)

mail = Mail(app)

from views import *

if __name__ == '__main__':
	app.run(debug=True)