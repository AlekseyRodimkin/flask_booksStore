from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
    Length
import sqlalchemy as sa
from app import db
from app.models import User


class LoginForm(FlaskForm):
    """Authorization Form class"""
    username = StringField('Имя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class RegistrationForm(FlaskForm):
    """Registration form class"""
    username = StringField('Имя: ', validators=[DataRequired()])
    telegram = StringField('Telegram: @...', validators=[])
    email = StringField('Email:', validators=[Email()])
    password = PasswordField('Пароль:', validators=[DataRequired()])
    password2 = PasswordField(
        'Повторите пароль:', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')

    def validate_username(self, username):
        """
        The function of checking an existing name
        :param username: username
        :return: not or error
        """
        user = db.session.scalar(sa.select(User).where(
            User.username == username.data))
        if user is not None:
            raise ValidationError('Имя занято')

    def validate_email(self, email):
        """
        The function of checking an existing email
        :param email: email address
        :return: not or error
        """
        user = db.session.scalar(sa.select(User).where(
            User.email == email.data))
        if user is not None:
            raise ValidationError('Почта уже зарегистрирована')

    def validate_telegram(self, telegram):
        """
        The function of checking an existing telegram
        :param telegram: telegram address
        :return: not or error
        """
        if telegram.data:
            user = db.session.scalar(sa.select(User).where(
                User.telegram == telegram.data))
            if user is not None:
                raise ValidationError('Аккаунт с этим Telegram уже зарегистрирован')
