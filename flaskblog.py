from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '987aaf573ec33656fdad44edd26639ee6b34e34cea609e6336deec30044385a5'

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


@app.route('/about')
def about():
    return render_template('about.html', title="About")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title="Login", form=form)


if __name__ == '__main__':
    app.run(debug=True)
