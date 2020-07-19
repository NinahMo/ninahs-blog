from flask import Flask,render_template,url_for
app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)


