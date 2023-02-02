from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from scripts.litvar_api import litvar_url

from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, redirect, url_for, request, session, flash

from flask_sqlalchemy import SQLAlchemy

# from sqlalchemy.orm import backref, relationship
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Table, Column, Integer, ForeignKey
# from sqlalchemy.sql.schema import UniqueConstraint

from flask_login import (
    LoginManager,
    login_required,
    UserMixin,
    login_user,
    logout_user,
    current_user,
)
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SECRET_KEY"] = "superSecret"

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(80))


class variant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rs_id = db.Column(db.String(20), primary_key=True)
    gene = db.Column(db.String(20), nullable=False)
    diseases = db.Column(db.String(20))

    def __init__(self, rs_id, gene, diseases):
        self.rs_id = rs_id
        self.gene = gene
        self.diseases = diseases


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class LoginForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[validators.InputRequired(), validators.Length(min=4, max=15)],
    )
    password = PasswordField(
        "Password",
        validators=[validators.InputRequired(), validators.Length(min=8, max=80)],
    )
    remember = BooleanField("remember me")
    submit = SubmitField("Submit")


class RegisterForm(FlaskForm):
    username = StringField(
        "New Username",
        validators=[validators.InputRequired(), validators.Length(min=4, max=15)],
    )
    password = PasswordField(
        "New Password",
        validators=[validators.InputRequired(), validators.Length(min=8, max=80)],
    )
    submit = SubmitField("Submit")


@app.route("/")
def index():
    login_form = LoginForm()
    return render_template("index.html", login_form=login_form)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    register_form = RegisterForm()
    login_form = LoginForm()

    if register_form.validate_on_submit():

        hashed_password = generate_password_hash(
            login_form.password.data, method="sha256"
        )
        user = User(username=register_form.username.data, password=hashed_password)

        try:
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return render_template(
                "home_page.html",
                register_form=register_form,
                login_form=login_form,
                logged_in_user=current_user.username,
            )
        except IntegrityError:
            db.session.rollback()
            flash("You are already registered, please log in")
            return redirect("/")

    print(register_form.errors)
    return render_template("signup.html", register_form=register_form)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Login page route."""
    register_form = RegisterForm()
    login_form = LoginForm()

    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user:
            if check_password_hash(user.password, login_form.password.data):
                login_user(user, remember=login_form.remember.data)
                return redirect(url_for("home"))

        flash("Invalid username or password")
        return redirect("/")

    return render_template(
        "home_page.html", register_form=register_form, login_form=login_form
    )


@app.route("/home_page")
@login_required
def home():
    return render_template("home_page.html", logged_in_user=current_user.username)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/rsID/", methods=["GET", "POST"])
@login_required
def rsID():
    if request.method == "POST":
        rsid = request.form["rs"]
        get_id_response = litvar_url(rsid)
        rs = str(rsid)
        print(rs.strip("##"))
        valid_id = get_id_response
        if valid_id != None:
            return render_template("rsID.html", get_id_response=litvar_url(rsid))
        else:
            return render_template("rsID.html", rs=rs)

        # store in database
        # else:
        #     try:
        #         db.session.add(new_litvar_info)
        #         db.session.add(new_gene)
        #         db.session.add(new_diseases)
        #         db.session.commit()
        #     except Exception as error:
        #         db.session.rollback()
        #         return '<h1>ERROR: {}</h1>'.format(error)
        #     return render_template('rsID.html', get_id_response =litvar_url(rsid))
    return render_template("rsID.html")


if __name__ == "__main__":
    app.run(debug=True)
