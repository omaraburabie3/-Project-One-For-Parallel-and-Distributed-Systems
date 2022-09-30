from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'photo_gallery'

mysql = MySQL(app)

@app.route("/", methods = ['GET', 'POST'])
@app.route("/add_image/", methods = ['GET', 'POST'])
def add_image():
    if request.method == 'POST':
        key = request.form['key']
        name = request.form['name']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO image(image_key, image_name) VALUES(%s, %s)", (key, name))
        mysql.connection.commit()
        cursor.close()
    return render_template("add_image.html")

@app.route("/show_image/")
def show_image():
    return render_template("show_image.html")

@app.route("/show_keys/")
def show_keys():
    return render_template("show_keys.html")

@app.route("/memory_configuration/", methods = ['GET', 'POST'])
def memory_configuration():
    if request.method == 'POST':
        capacity = request.form['capacity']
        replacement_policy = request.form['replacement-policy']
        clear_cache = request.form['clear-cache']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO memory_configuration(capacity, replacement_policy, clear_cache) VALUES(%s, %s, %s)", (capacity, replacement_policy, clear_cache))
        mysql.connection.commit()
        cursor.close()
    return render_template("memory_configuration.html")

@app.route("/memory_statistics/")
def memory_statistics():
    return render_template("memory_statistics.html")

"""
@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
"""

app.run(host='localhost', port=5000)