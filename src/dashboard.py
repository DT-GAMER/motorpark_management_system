from flask import Flask, render_template, request, redirect, url_for, session

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

@app.route('/dashboard')

def dashboard():

    if 'admin' in session:

        cursor = conn.execute('SELECT COUNT(*) FROM drivers')

        num_drivers = cursor.fetchone()[0]

        cursor = conn.execute('SELECT COUNT(*) FROM car_owners')

        num_car_owners = cursor.fetchone()[0]

        cursor = conn.execute('SELECT COUNT(*) FROM cars')

        num_cars = cursor.fetchone()[(0]

                                      

