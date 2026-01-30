from flask import Flask,render_template

app = Flask(__name__)

post = [
    {
        'author': 'Turja',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2024'
    },
    {
        'author': 'Turja',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2024'
    }
]

@app.route("/")
@app.route("/home")
def hello_world():
    return render_template('home.html', posts=post)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)