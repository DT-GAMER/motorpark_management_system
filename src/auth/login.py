from flask import Flask, render_template, request, redirect, url_for, session, flash
import hashlib
import sqlite3

app = Flask(__name__)

# connect to database
conn = sqlite3.connect('database.db')

@app.route('/')
def home():
    if 'admin' in session:
        return render_template('dashboard.html')
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # validate input data
        if email == '' or password == '':
            flash('All fields are required.')
            return redirect(url_for('login'))
        
        # hash password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        # check if email and password match
        cursor = conn.execute('SELECT * FROM car_owners WHERE email=? AND password=?', (email, hashed_password))
        result = cursor.fetchone()
        if result:
            session['admin'] = email
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password.')
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect(url_for('login'))
