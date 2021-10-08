from flask import *
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = YOUR_SECRET_KEY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    map_url = db.Column(db.String(500), unique=True, nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    has_sockets = db.Column(db.String(5), nullable=False)
    has_toilet = db.Column(db.String(5), nullable=False)
    has_wifi = db.Column(db.String(5), nullable=False)
    can_take_calls = db.Column(db.String(5), nullable=False)
    seats = db.Column(db.String(10), nullable=False)
    coffee_price = db.Column(db.String(10), nullable=False)


class AddForm(FlaskForm):
    name = StringField("Name:", render_kw={'class': 'form-control'}, validators=[DataRequired()])
    map_url = StringField("Map URL:", render_kw={'class': 'form-control'}, validators=[DataRequired(), URL()])
    img_url = StringField("Image URL:", render_kw={'class': 'form-control'}, validators=[DataRequired(), URL()])
    location = StringField("Location:", render_kw={'class': 'form-control'}, validators=[DataRequired()])
    sockets = SelectField("Cafe has sockets (1 for Yes, 0 for No):", choices=["0", "1"],
                          render_kw={'class': 'form-control'}, validators=[DataRequired()])
    toilet = SelectField("Cafe has toilet (1 for Yes, 0 for No):", choices=["0", "1"],
                         render_kw={'class': 'form-control'}, validators=[DataRequired()])
    wifi = SelectField("Cafe has WiFi (1 for Yes, 0 for No):", choices=["0", "1"],
                       render_kw={'class': 'form-control'}, validators=[DataRequired()])
    calls = SelectField("Can take calls in the cafe (1 for Yes, 0 for No):", choices=["0", "1"],
                        render_kw={'class': 'form-control'}, validators=[DataRequired()])
    seats = StringField("No. of seats:", render_kw={'class': 'form-control'}, validators=[DataRequired()])
    coffee_price = StringField("Coffee Price:", render_kw={'class': 'form-control'}, validators=[DataRequired()])
    submit = SubmitField("Submit", render_kw={'class': 'btn btn-primary btn-md'})


class DelForm(FlaskForm):
    name = StringField(label="Name", render_kw={'class': 'form-control'}, validators=[DataRequired()])
    submit = SubmitField("Submit", render_kw={'class': 'btn btn-primary btn-md'})


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cafe-list")
def cafe_list():
    cafes = Cafe.query.all()
    # print(cafes)
    return render_template("cafe-list.html", cafes=cafes)


@app.route("/add-cafe", methods=["GET", "POST"])
def add():
    form = AddForm()
    if request.method == "GET":
        return render_template("add.html", form=form)
    else:
        new_cafe = Cafe(name=form.name.data, map_url=form.map_url.data, img_url=form.img_url.data,
                        location=form.location.data, has_sockets=form.sockets.data, has_toilet=form.toilet.data,
                        has_wifi=form.wifi.data, can_take_calls=form.calls.data, seats=form.seats.data,
                        coffee_price=form.coffee_price.data)
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for("cafe_list"))


@app.route("/delete-cafe", methods=["GET", "POST"])
def delete():
    form = DelForm()
    if request.method == "GET":
        return render_template("delete.html", form=form)
    else:
        rem_cafe = Cafe.query.filter_by(name=form.name.data).first()
        db.session.delete(rem_cafe)
        db.session.commit()
        return redirect(url_for("cafe_list"))


if __name__ == "__main__":
    app.run(debug=True)
