from flask import Flask, redirect, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route("/buffets")
def buffets():
    return render_template("buffets.html")

@app.route("/pricing&hours")
def login():
    return render_template("pricing.html")

@app.route("/reservations")
def about():
    return render_template("reservations.html")

@app.route("/location")
def contact():
    return render_template("location.html")

@app.route("/bookatable")
def book_now():
    return render_template("bookatable.html")

@app.route('/login', methods=['POST'])
def login_user():
    username = request.form.get('username')
    password = request.form.get('password')
    return redirect(url_for('booking'))

@app.route('/booking')
def booking():
    return render_template('booking.html')

if __name__ == '__main__':
    app.run(debug=True) 