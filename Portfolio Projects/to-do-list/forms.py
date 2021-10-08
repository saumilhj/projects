from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddListForm(FlaskForm):
    list_name = StringField(validators=[DataRequired()])
    submit = SubmitField("Submit")


class AddItemForm(FlaskForm):
    item_name = StringField(validators=[DataRequired()])
    add = SubmitField("Add")