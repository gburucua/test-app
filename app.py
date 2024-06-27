from flask import Flask, render_template, request, redirect
from database import MySQLDatabase

app = Flask(__name__)

# Initialize the MySQL database connection
db = MySQLDatabase()

@app.route('/')
def index():
    with app.app_context():
        users = db.execute_query("SELECT * FROM users")
    return render_template('index.html', users=users)

@app.route('/users')
def user_list():
    users = db.execute_query("SELECT * FROM users")
    return render_template('user_list.html', users=users)

@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form['username']
    email = request.form['email']
    query = f"INSERT INTO users (username, email) VALUES ('{username}', '{email}')"
    with app.app_context():
        db.execute_query(query)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
