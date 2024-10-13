import flask
import db
import bcrypt
import unidecode


Administratif = flask.Blueprint('Administratif', __name__)


conf = {
    'user': ["Compte", "Affectation", "Annuaire"],
    'rh': ["Compte", "Administratif", "Affectation", "Service", "Annuaire"],
    'admin': ["Compte", "Administratif", "Affectation", "Service", "Annuaire"]
}


@Administratif.route('/', methods=['POST', 'GET'])
def administratif():
    if 'login' not in flask.session or 'Administratif' not in conf[flask.session['role']]:
        return flask.redirect(flask.url_for("index"))
    if flask.request.method == 'GET':
        return flask.render_template('Administratif/Administratif.html', user_co=db.get_user(flask.session['login']),
                                     us=db.get_personnes(), nav=conf[flask.session['role']],
                                     nom=flask.session['login'], groupe=flask.session['role'])
    else:
        recherche = unidecode.unidecode(flask.request.form.get('recherche').lower())
        us = db.get_personnes()
        val = []
        for i in us:
            if recherche in unidecode.unidecode(i["nom"].lower()) or recherche in unidecode.unidecode(
                    i["prenom"].lower()):
                val.append(i)
        return flask.render_template('Administratif/Administratif.html', user_co=db.get_user(flask.session['login']),
                                     us=val, nav=conf[flask.session['role']],
                                     nom=flask.session['login'], groupe=flask.session['role'])


@Administratif.route('/update/<login>', methods=['POST', 'GET'])
def Administratif_update(login):
    if 'login' not in flask.session or 'Administratif' not in conf[flask.session['role']]:
        return flask.redirect(flask.url_for("index"))
    if flask.request.method == 'GET':
        return flask.render_template('Administratif/Administratif_update.html', user_co=db.get_user(flask.session['login']),
                                     user=db.get_user(login), nav=conf[flask.session['role']],
                                     nom=flask.session['login'], groupe=flask.session['role'],
                                     user_nbr=db.get_user_nbrposte(login),
                                     user_info=db.get_user_compte(login))

    else:
        user = db.get_user(login)

        nom = flask.request.form.get('nom') or user['nom']
        prenom = flask.request.form.get('prenom') or user['prenom']
        naissance = flask.request.form.get('naissance') or user['naissance']
        statut = flask.request.form.get('statut') or user['statut']
        email_uga = flask.request.form.get('email_uga') or user['email_uga']
        login_nouveau = flask.request.form.get('login_nouveau') or user['login']
        email_perso = flask.request.form.get('email_perso') or user['email_perso']
        tel_perso = flask.request.form.get('tel_perso') or user['tel_perso']
        adresse_perso = flask.request.form.get('adresse_perso') or user['adresse_perso']

        list_user = {
            "login": login,
            "nom": nom,
            "prenom": prenom,
            "naissance": naissance.replace("/", "-"),
            "statut": statut,
            "email_uga": email_uga,
            "login_nouveau": login_nouveau,
            "email_perso": email_perso,
            "tel_perso": tel_perso,
            "adresse_perso": adresse_perso,
        }

        db.update_user(list_user)
        return flask.redirect(flask.url_for('Administratif_update', login=login_nouveau))


@Administratif.route('/remove/<login>')
def Administratif_remove(login):
    if 'login' not in flask.session or 'Administratif' not in conf[flask.session['role']]:
        return flask.redirect(flask.url_for("index"))
    db.del_user(login)
    return flask.redirect(flask.url_for('Administratif.administratif'))


@Administratif.route('/add', methods=['POST', 'GET'])
def Administratif_add():
    if 'login' not in flask.session or 'Administratif' not in conf[flask.session['role']]:
        return flask.redirect(flask.url_for("index"))
    if flask.request.method == 'GET':
        return flask.render_template('Administratif/Administratif_add.html', nav=conf[flask.session['role']],
                                     nom=flask.session['login'], user_co=db.get_user(flask.session['login']),
                                     groupe=flask.session['role'])
    else:

        nom = flask.request.form.get('nom')
        prenom = flask.request.form.get('prenom')
        naissance = flask.request.form.get('naissance')
        statut = flask.request.form.get('statut')
        email_uga = flask.request.form.get('email_uga')
        secu = flask.request.form.get('secu')
        login = flask.request.form.get('login')
        mdp = flask.request.form.get('mdp')

        mdp = bcrypt.hashpw(mdp.encode('utf-8'), bcrypt.gensalt()).decode("utf-8")

        role = flask.request.form.get('role')
        email_perso = flask.request.form.get('email_perso')
        tel_perso = flask.request.form.get('tel_perso')
        adresse_perso = flask.request.form.get('adresse_perso')

        list_user = {
            "nom": nom,
            "prenom": prenom,
            "naissance": naissance,
            "statut": statut,
            "email_uga": email_uga,
            "secu": secu,
            "login": login,
            "mdp": mdp,
            "role": role,
            "email_perso": email_perso,
            "tel_perso": tel_perso,
            "adresse_perso": adresse_perso,
        }

    verif = db.add_user(list_user)

    return flask.render_template('Administratif/Administratif_add.html', nav=conf[flask.session['role']],
                                 nom=flask.session['login'], user_co=db.get_user(flask.session['login']),
                                 groupe=flask.session['role'], verif=verif)

