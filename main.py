from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost' # Which host are we using (need to changed for the deployment)
app.config['MYSQL_USER'] = 'root' # Level of access
app.config['MYSQL_PASSWORD'] = '' # Password of the database
app.config['MYSQL_DB'] = 'flask'  # This is the name of database

mysql = MySQL(app)


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        cursor = mysql.connection.cursor()
        cursor.execute(
            ''' INSERT INTO info_table VALUES(%s,%s)''', (name, age))
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"


app.run(host='localhost', port=5000)
