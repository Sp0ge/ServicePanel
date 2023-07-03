from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from flask_wtf import FlaskForm


class User_Add(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired(), EqualTo('password_confirm')])
    password_confirm = PasswordField('Пароль Повторно', validators=[DataRequired()])
    submit = SubmitField("Создать")
    
class User_log(FlaskForm):
    username = StringField('Логин')
    password = PasswordField('Пароль')
    remember_me = BooleanField("Запомнить", default = False)
    submit = SubmitField("войти")


class WebApps_add(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    description = StringField('Описание', validators=[DataRequired()])
    url = StringField('Ссылка на сервис', validators=[DataRequired()])
    img_url = StringField('Ссылка на картинку', validators=[DataRequired()])
    submit = SubmitField("Добавить")
