from flask import Blueprint, render_template, request,redirect, flash, url_for
from app.models import Oracle

auth = Blueprint('auth', __name__)
oracle_db = Oracle()
@auth.route('/', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        nm_usuario = request.form.get('nm_usuario')
        if nm_usuario:
            validation = oracle_db.user_login(nm_usuario)
            if validation == True:
                return redirect(url_for('views.gestao'))
                print('Validação efetuada.')
            else:
                flash('Falha na autenticação do usuário.', category='error')
        else:
            flash('Usuário não informado!', category='error')
    return render_template("login.html")