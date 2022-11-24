from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost' # Which host are we using (need to changed for the deployment)
app.config['MYSQL_USER'] = 'root' # 
app.config['MYSQL_PASSWORD'] = '' 
app.config['MYSQL_DB'] = 'flask'  # This it the name of database

mysql = MySQL(app)
