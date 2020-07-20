from flask import render_template,url_for,flash,redirect
from flaskblog import app,db,bcrypt
from flaskblog.forms import RegistrationForm,LoginForm 
from flaskblog.models import User,Post



posts = [
    {
        'author': 'Ninah Mozzy',
        'title': 'Blog post 1',
        'content': 'Hello Loves',
        'date_posted': 'April 1, 2020'
    },
    {
        'author': 'simpo boy',
        'title': 'Blog post 2',
        'content': 'Ndio manake',
        'date_posted': 'April 4, 2020'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST']) 
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == '' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


