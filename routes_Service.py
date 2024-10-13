import flask
import flask_wtf

import db
import routes_map

import sqlite3
import click

import bcrypt
import unidecode


Service = flask.Blueprint('Service', __name__)


conf = {
    'user': ["Compte", "Affectation", "Annuaire"],
    'rh': ["Compte", "Administratif", "Affectation", "Service", "Annuaire"],
    'admin': ["Compte", "Administratif", "Affectation", "Service", "Annuaire"]
}


@Service.route('/', methods=['POST', 'GET'])
def service():
    if 'login' not in flask.session or 'Service' not in conf[flask.session['role']]:
        return flask.redirect(flask.url_for("index"))
    if flask.request.method == 'GET':
        return flask.render_template('Service/Service.html', user_co=db.get_user(flask.session['login']),
                                     services=db.get_services(), nav=conf[flask.session['role']],
                                     nom=flask.session['login'], groupe=flask.session['role'])
    else:
        recherche = unidecode.unidecode(flask.request.form.get('recherche').lower())
        services = db.get_services()
        val = []
        for i in services:
            if recherche in unidecode.unidecode(i["nom"].lower()):
                val.append(i)
        return flask.render_template('Service/Service.html', user_co=db.get_user(flask.session['login']),
                                     services=val, nav=conf[flask.session['role']],
                                     nom=flask.session['login'], groupe=flask.session['role'])


@Service.route('/remove/<code>')
def Service_remove(code):
    if 'login' not in flask.session or 'Service' not in conf[flask.session['role']]:
        return flask.redirect(flask.url_for("index"))

    db.del_services(code)
    return flask.redirect(flask.url_for('Service.service'))


@Service.route('/update/<code>', methods=['POST', 'GET'])
def Service_update(code):
    if 'login' not in flask.session or 'Service' not in conf[flask.session['role']]:
        return flask.redirect(flask.url_for("index"))
    if flask.request.method == 'GET':
        return flask.render_template('Service/Service_update.html', nav=conf[flask.session['role']],
                                     nom=flask.session['login'], user_co=db.get_user(flask.session['login']),
                                     groupe=flask.session['role'], service=db.get_service_vue(code),
                                     structures=db.get_structures(), nbr_utilisateur=db.get_nbrutilisateur(code))
    else:
        services = db.get_service_vue(code)

        nom = flask.request.form.get('nom') or services['nom']
        tel = flask.request.form.get('tel') or services['tel']
        email = flask.request.form.get('email') or services['email']
        type = flask.request.form.get('type') or services['type']
        new_code_structures = flask.request.form.get('new_code_structures') or code

        service = {
            "code": code,
            "nom": nom,
            "tel": tel,
            "email": email,
            "type": type,
            "new_code_structures": new_code_structures,
        }

        db.update_services(service)
        return flask.redirect(flask.url_for('Service.Service_update', code=code))


@Service.route('/add', methods=['POST', 'GET'])
def Service_add():
    if 'login' not in flask.session or 'Service' not in conf[flask.session['role']]:
        return flask.redirect(flask.url_for("index"))
    if flask.request.method == 'GET':
        return flask.render_template('Service/Service_add.html', nav=conf[flask.session['role']],
                                     nom=flask.session['login'], user_co=db.get_user(flask.session['login']),
                                     groupe=flask.session['role'], structures=db.get_structures())
    else:
        code = flask.request.form.get('code')
        nom = flask.request.form.get('nom')
        tel = flask.request.form.get('tel')
        email = flask.request.form.get('email')
        type = flask.request.form.get('type')
        code_structure = flask.request.form.get('code_structure')

        service = {
            "code": code,
            "nom": nom,
            "tel": tel,
            "email": email,
            "type": type,
            "code_structure": code_structure,
        }

        verif = db.add_services(service)
        return flask.render_template('Service/Service_add.html', nav=conf[flask.session['role']], verif=verif,
                                     nom=flask.session['login'], user_co=db.get_user(flask.session['login']),
                                     groupe=flask.session['role'], structures=db.get_structures())


