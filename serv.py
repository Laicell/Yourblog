from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Charlie Shuffler',
        'title': 'Post 1',
        'content': 'Первый пост',
        'date_posted': 'Март 20, 2019'
    },
    {
        'author': 'Jane Logan',
        'title': 'Post 2',
        'content': 'Второй пост',
        'date_posted': 'Март 21, 2019'
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

