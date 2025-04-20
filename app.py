#from flask import Flask,
#render_template, request

#app = Flask(__name__)

#@app.route('/')
#def index():
 #   return render_template('index.html', user_name="Guest")

#if __name__ == '__main__':
 #   app.run(debug=True)

#  from flask import Flask, render_template, request

#   app = Flask(__name__)

#   @app.route('/')
#   def home():
#      return render_template('index.html')

#   @app.route('/register', methods=['GET', 'POST'])
#   def register():
#      if request.method == 'POST':
#          username = request.form['username']
#          email = request.form['email']
#          password = request.form['password']
#          print(f"User Registered: {username}, {email}, {password}")
#          return "Registration successful!"
#      return render_template('register.html')

#   if __name__ == '__main__':
#      app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

@app.route('/')
def home():
    return render_template('index.html')  # Or your home page file

# ------------------ Register Route ------------------

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']
        username = request.form['username']
        password = request.form['password']
        confirm = request.form['confirm_password']

        if password != confirm:
            flash('Passwords do not match!', 'error')
            return redirect(url_for('register'))

        # TODO: Save user data to database
        # You can print it for now as a placeholder
        print(f"New user: {fullname}, {email}, {phone}, {username}")

        flash('Registration successful!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # TODO: Authenticate user (you can add logic here later)
        if username == "admin" and password == "admin":
            flash("Login successful!", "success")
            return redirect(url_for('home'))
        else:
            flash("Invalid username or password", "error")
            return redirect(url_for('login'))

    return render_template('login.html')

if __name__ == '__main__':
     app.run(debug=True)