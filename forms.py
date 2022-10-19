from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, BooleanField, validators, Form
from wtforms.validators import DataRequired, Length, Email
from wtforms.widgets import TextArea, TextInput


class FormContato(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    assunto = StringField('Assunto', validators=[DataRequired(), Length(1, 30)])
    descricao = StringField('Descrição do assunto', validators=[validators.Optional()], widget=TextArea())
    lembrar_dados = BooleanField('Lembrar dados de acesso')
    botao_submit = SubmitField('Enviar Mensagem')

