from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'afc48752f0fd9292ddc603a09a25f65e'

posts = [
        {
            'author': 'Rory Mackintosh',
            'title': 'Blog Post 1',
            'content': 'First post content',
            'date_posted': 'October 28, 2022'
        },
        {
            'author': 'Amy Dickson',
            'title': 'Blog Post 2',
            'content': 'Second post content',
            'date_posted': 'October 29, 2022'
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
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'rorymac126@gmail.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
