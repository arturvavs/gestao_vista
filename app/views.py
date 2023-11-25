#Nesse arquivo ficam as Views que 'redirecionam' o usuário para cada página do website
#Por exemplo, podemos ter uma view '/home' na qual caso o usuário digite 'facebook.com/home', o site será direcionado para essa página

from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("login.html")

@views.route('/gestao')
def gestao():
    return render_template("gestao.html")