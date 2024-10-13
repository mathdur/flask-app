# routes_map.py : Blueprint pour afficher une liste des routes de l'application Flask

import flask
import db

map_bp = flask.Blueprint('map_bp', __name__)

conf = {
    'user': ["Compte", "Annuaire"],
    'rh': ["Compte", "Administratif", "Affectation", "Service", "Annuaire"],
    'admin': ["Compte", "Administratif", "Affectation", "Service", "Annuaire"]
}

def site_map(url_map):
    """Plan d'un site sous forme d'une liste 2D contenant la description de
    chaque route de forme ``{'route': "/", 'endpoint': "index", 'methods': "GET, POST", 'url': "/" (si possible)}``.
    """

    def has_no_empty_params(rule):
        """Détecte la présence de paramètres sans valeur par défaut"""
        defaults = rule.defaults if rule.defaults is not None else ()
        arguments = rule.arguments if rule.arguments is not None else ()
        return len(defaults) >= len(arguments)

    links = []
    for rule in url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if rule.endpoint == 'static':
            continue
        methods = [r for r in rule.methods if r not in ["OPTIONS", "HEAD"]]
        link = {'route': rule.rule, 'endpoint': rule.endpoint, 'methods': ", ".join(methods), 'url': None}
        if "GET" in rule.methods and has_no_empty_params(rule):
            link['url'] = flask.url_for(rule.endpoint, **(rule.defaults or {}))
        links.append(link)
    return links


@map_bp.route("/")
def map_index():
    links = site_map(flask.current_app.url_map)
    return flask.render_template('map/map.html', links=links, user_co=db.get_user(flask.session['login']), nav=conf[flask.session['role']],)