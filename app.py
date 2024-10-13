import flask
import flask_wtf

import db
import routes_map
import routes_Administratif
import routes_Affectation
import routes_Service

import sqlite3
import click

import bcrypt
import unidecode

app = flask.Flask(__name__)
app.config.from_pyfile('config.py')

app.config['TEMPLATES_AUTO_RELOAD'] = True  # Ligne a enlever

app.teardown_appcontext(db.close_db)
flask_wtf.csrf.CSRFProtect(app)

app.register_blueprint(routes_map.map_bp, url_prefix='/map')
app.register_blueprint(routes_Administratif.Administratif, url_prefix='/Administratif')
app.register_blueprint(routes_Affectation.Affectation, url_prefix='/Affectation')
app.register_blueprint(routes_Service.Service, url_prefix='/Service')

conf = {
    'user': ["Compte", "Affectation", "Annuaire"],
    'rh': ["Compte", "Administratif", "Affectation", "Service", "Annuaire"],
    'admin': ["Compte", "Administratif", "Affectation", "Service", "Annuaire"]
}


@app.route('/', methods=['POST', 'GET'])
def index():
    if 'login' in flask.session:
        return flask.redirect(flask.url_for('Compte'))
    if flask.request.method == 'GET':
        return flask.render_template('index.html')
    else:
        login = flask.request.form.get('login')
        password = flask.request.form.get('password')
        if check_login(login, password) == True:
            user = db.get_role(login)
            flask.session['login'] = login
            flask.session['role'] = user['role']
        return flask.redirect(flask.url_for('index'))


def check_login(login, password):
    user = db.check(login)
    return user is not None and password_verify(password, user['mdp'])


def password_verify(password, hash):
    return bcrypt.checkpw(password.encode('utf-8'),
                          hash.encode('utf-8') if isinstance(hash, str) else hash)


@app.route('/logout')
def logout():
    if 'login' in flask.session:
        flask.session.pop('login')
    return flask.redirect(flask.url_for('index'))


@app.route('/Compte', methods=['POST', 'GET'])
def Compte():
    if 'login' not in flask.session:
        return flask.redirect(flask.url_for("index"))
    if flask.request.method == 'GET':
        return flask.render_template('Compte.html', user_co=db.get_user(flask.session['login']),
                                     nav=conf[flask.session['role']],
                                     nom=flask.session['login'], groupe=flask.session['role'],
                                     user_nbr=db.get_user_nbrposte(flask.session['login']),
                                     user_info=db.get_user_compte(flask.session['login']))
    else:
        user = db.get_user(flask.session['login'])

        email_perso = flask.request.form.get('email_perso') or user['email_perso']
        tel_perso = flask.request.form.get('tel_perso') or user['tel_perso']
        adresse_perso = flask.request.form.get('adresse_perso') or user['adresse_perso']

        list_user = {
            "login": flask.session['login'],
            "email_perso": email_perso,
            "tel_perso": tel_perso,
            "adresse_perso": adresse_perso,
        }

        db.update_user_acceuil(list_user)
        return flask.redirect(flask.url_for('Compte'))




@app.route('/Annuaire', methods=['POST', 'GET'])
def Annuaire():
    if 'login' not in flask.session:
        return flask.redirect(flask.url_for("index"))
    if flask.request.method == 'GET':
        return flask.render_template('Annuaire.html', user_co=db.get_user(flask.session['login']),
                                     us=db.get_affectation_vue(), nav=conf[flask.session['role']],
                                     nom=flask.session['login'], groupe=flask.session['role'])
    else:
        recherche = unidecode.unidecode(flask.request.form.get('recherche').lower())
        us = db.get_affectation_vue()
        val = []
        for i in us:
            if recherche in unidecode.unidecode(i["nom"].lower()) or recherche in unidecode.unidecode(
                    i["prenom"].lower()):
                val.append(i)
        return flask.render_template('Annuaire.html', user_co=db.get_user(flask.session['login']),
                                     us=val, nav=conf[flask.session['role']],
                                     nom=flask.session['login'], groupe=flask.session['role'])

@app.errorhandler(404)
def page_not_found(error):
    if 'login' not in flask.session:
        return flask.redirect(flask.url_for('index'))
    else:
        return flask.redirect(flask.url_for('Compte'))



@app.cli.command("initdb")
@click.argument("sql_file", default="data/dump_db.sql")
def init_db(sql_file):
    print(f"*** Initialisation de la base de données {app.config['DATABASE']} ***")
    db = sqlite3.connect(app.config['DATABASE'])
    cursor = db.cursor()
    with open(sql_file, encoding='utf8') as file:
        cursor.executescript(file.read())
        db.commit()
    db.close()


if __name__ == '__main__':
    app.run(port=5000, debug=True)
