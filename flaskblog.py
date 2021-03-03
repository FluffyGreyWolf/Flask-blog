from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Some one',
        'title': 'Blog Post 1',
        'content': 'First blog content',
        'date_posted': 'April 20, 2020'
    },
    {
        'author': 'Some two',
        'title': 'Blog Post 2',
        'content': 'Second blog content',
        'date_posted': 'April 25, 2021'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@ app.route('/about')
def about():
    return render_template('about.html', title="About")


if __name__ == '__main__':
    app.run(debug=True)
