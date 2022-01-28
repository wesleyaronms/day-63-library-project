from wtforms.validators import DataRequired, NumberRange
from wtforms import StringField, FloatField, SubmitField
from flask_wtf import FlaskForm


message = "Este campo não pode ficar em branco."


class BooksForm(FlaskForm):
    book_title = StringField(label="Book Name", validators=[DataRequired(message=message)])
    book_author = StringField(label="Author Name", validators=[DataRequired(message=message)])
    book_rating = FloatField(label="Rating",
                             validators=[DataRequired(message=message),
                                         NumberRange(min=0, max=10, message="A pontuação deve estar entre 0 e 10.")])
    submit = SubmitField("Add Book")


class EditForm(FlaskForm):
    new_rating = FloatField(label="New Rating",
                            validators=[DataRequired(message=message),
                                        NumberRange(min=0, max=10, message="A pontuação deve estar entre 0 e 10.")])
    submit = SubmitField("Change Rating")
