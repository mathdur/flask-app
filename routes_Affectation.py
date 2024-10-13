import flask
import db
import unidecode


Affectation = flask.Blueprint('Affectation', __name__)


conf = {
    'user': ["Compte", "Affectation", "Annuaire"],
    'rh': ["Compte", "Administratif", "Affectation", "Service", "Annuaire"],
    'admin': ["Compte", "Administratif", "Affectation", "Service", "Annuaire"]
}



@Affectation.route('/', methods=['POST', 'GET'])
def affectation():
    if 'login' not in flask.session or 'Affectation' not in conf[flask.session['role']]:
        return flask.redirect(flask.url_for("index"))
    if flask.request.method == 'GET':
        return flask.render_template('Affectation/Affectation.html', users=db.get_affectation_vue(),
                                     nav=conf[flask.session['role']],
                                     nom=flask.session['login'], user_co=db.get_user(flask.session['login']),
                                     groupe=flask.session['role'])
    else:
        recherche = unidecode.unidecode(flask.request.form.get('recherche').lower())
        users = db.get_affectation_vue()
        val = []
        for i in users:
            if recherche in unidecode.unidecode(i["nom"].lower()) or recherche in unidecode.unidecode(
                    i["prenom"].lower()):
                val.append(i)
        return flask.render_template('Affectation/Affectation.html', users=val, nav=conf[flask.session['role']],
                                     nom=flask.session['login'], user_co=db.get_user(flask.session['login']),
                                     groupe=flask.session['role'])


@Affectation.route('/remove/<numero>')
def Affectation_remove(numero):
    if 'login' not in flask.session or 'Affectation' not in conf[flask.session['role']]:
        return flask.redirect(flask.url_for("index"))

    db.del_affectation(numero)
    return flask.redirect(flask.url_for('Affectation.affectation'))


@Affectation.route('/update/<numero>', methods=['POST', 'GET'])
def Affectation_update(numero):
    if 'login' not in flask.session or 'Affectation' not in conf[flask.session['role']]:
        return flask.redirect(flask.url_for("index"))
    if flask.request.method == 'GET':
        login = db.get_login_num(numero)
        return flask.render_template('Affectation/Affectation_update.html', nav=conf[flask.session['role']],
                                     users=db.get_affectation_vue(),
                                     nom=flask.session['login'], user_aff=db.get_user(login['login']),
                                     user_co=db.get_user(flask.session['login']),
                                     groupe=flask.session['role'], services=db.get_service(),
                                     personnes=db.get_personnes(),
                                     user_nbr=db.get_user_nbrposte(login['login']),
                                     user_info=db.get_user_compte(login['login']),
                                     info=db.get_user_affectation_vue(numero),
                                     select=db.get_user(login['login'])['prenom'] + " " + db.get_user(login['login'])[
                                         'nom'])
    else:
        user = db.get_user_affectation_vue(numero)

        secu = user['secu']
        debut = flask.request.form.get('debut').replace("/", "-") or user['debut']
        fin = flask.request.form.get('fin').replace("/", "-") or user['fin']
        poste = flask.request.form.get('poste') or user['poste']
        service = flask.request.form.get('service') or user['service']
        tel = flask.request.form.get('tel') or user['tel']
        tempstravail = flask.request.form.get('tempstravail') or user['tempstravail']

        list_user = {
            "numero": numero,
            "secu": secu,
            "debut": debut,
            "fin": fin,
            "poste": poste,
            "service": service,
            "tel": tel,
            "tempstravail": tempstravail,
        }

        db.update_affectation(list_user)
        return flask.redirect(flask.url_for('Affectation.Affectation_update', numero=numero))

def test(login):
    personnes = db.get_personnes()
    for user in personnes:
        if login == user['login']:
            return True
    return False

@Affectation.route('/add/<login>', methods=['POST', 'GET'])
def Affectation_add(login):
    if 'login' not in flask.session or 'Affectation' not in conf[flask.session['role']]:
        return flask.redirect(flask.url_for("index"))
    if flask.request.method == 'GET':
        rep = test(login)
        if rep == True:
            return flask.render_template('Affectation/Affectation_add.html', nav=conf[flask.session['role']],
                                     users=db.get_affectation_vue(),
                                     nom=flask.session['login'], user_aff=db.get_user(login),
                                     services=db.get_service(),
                                     personnes=db.get_personnes(),
                                     user_co=db.get_user(flask.session['login']),
                                     user_nbr=db.get_user_nbrposte(login),
                                     user_info=db.get_user_compte(login),
                                     select=db.get_user(login)['prenom'] + " " + db.get_user(login)['nom'])
        else:
            login = db.get_rdm_user()['login']
            return flask.render_template('Affectation/Affectation_add.html', nav=conf[flask.session['role']],
                                         users=db.get_affectation_vue(),
                                         nom=flask.session['login'], user_aff=db.get_user(login),
                                         services=db.get_service(),
                                         personnes=db.get_personnes(),
                                         user_co=db.get_user(flask.session['login']),
                                         user_nbr=db.get_user_nbrposte(login),
                                         user_info=db.get_user_compte(login),
                                         select=db.get_user(login)['prenom'] + " " + db.get_user(login)['nom'])

    else:

        debut = flask.request.form.get('debut')
        fin = flask.request.form.get('fin')
        poste = flask.request.form.get('poste')
        secu = db.get_user(login)['secu']
        service = flask.request.form.get('service')
        tel = flask.request.form.get('tel')
        tempstravail = flask.request.form.get('tempstravail')

        list_user = {
            "debut": debut.replace("/", "-"),
            "fin": fin.replace("/", "-"),
            "poste": poste,
            "secu": secu,
            "service": service,
            "tel": tel,
            "tempstravail": tempstravail,
        }

        verif = db.add_affectation(list_user)
        return flask.render_template('Affectation/Affectation_add.html', nav=conf[flask.session['role']],
                                     users=db.get_affectation_vue(),
                                     nom=flask.session['login'], user_co=db.get_user(login),
                                     groupe=flask.session['role'], services=db.get_service(),
                                     personnes=db.get_personnes(),
                                     user_nbr=db.get_user_nbrposte(login),
                                     user_info=db.get_user_compte(login),
                                     select=db.get_user(login)['prenom'] + " " + db.get_user(login)['nom'])