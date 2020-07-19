from flask import Flask,render_template,url_for
from forms import RegistrationForm,LoginForm 
app = Flask(__name__)

app.config['SECRET_KEY'] = '6fc3f5630eabfc72446c3246558089f7'

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

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True)


