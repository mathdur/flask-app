# db.py : manipulations de la base de données

import sqlite3
import flask


def get_db():
    if 'db' not in flask.g:
        flask.g.db = sqlite3.connect(flask.current_app.config['DATABASE'])
        flask.g.db.row_factory = sqlite3.Row
        flask.g.db.cursor().execute("PRAGMA foreign_keys = 1")
        flask.current_app.logger.info('Connexion à la BDD')
    return flask.g.db


def close_db(e=None):
    db = flask.g.pop('db', None)
    if db is not None:
        db.close()
        flask.current_app.logger.info('Déconnexion de la BDD')


def get_users():
    cursor = get_db().cursor()
    cursor.execute("""SELECT *
                      FROM comptes""")
    return cursor.fetchall()


def get_annuaire(prenom, service):
    cursor = get_db().cursor()
    if prenom == "" and service != "":
        cursor.execute("""SELECT *
    FROM affectations
    INNER JOIN services
    on services.code = affectations.service
    INNER JOIN personnes
    on personnes.secu = affectations.secu
    WHERE services.type = :service
    ORDER by personnes.prenom ASC""", {"service": service})

    elif prenom != "" and service == "":
        cursor.execute("""SELECT *
    FROM affectations
    INNER JOIN services
    on services.code = affectations.service
    INNER JOIN personnes
    on personnes.secu = affectations.secu
    WHERE personnes.prenom = :prenom""", {"prenom": prenom})

    elif (prenom and service) == "":
        cursor.execute("""SELECT *
            FROM affectations
            INNER JOIN services
            on services.code = affectations.service
            INNER JOIN personnes
            on personnes.secu = affectations.secu
            ORDER by services.type ASC""")

    elif (prenom and service) != "":
        cursor.execute("""SELECT *
            FROM affectations
            INNER JOIN services
            on services.code = affectations.service
            INNER JOIN personnes
            on personnes.secu = affectations.secu
            WHERE personnes.prenom = :prenom AND services.type = :service""", {"prenom": prenom, "service": service})

    return cursor.fetchall()


def get_user(login):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""SELECT * 
            FROM personnes  as p INNER JOIN comptes as c
            ON p.login = c.login
            WHERE p.login = :login""", {'login': login})
    return cursor.fetchone()


def get_personnes():
    cursor = get_db().cursor()
    cursor.execute("""SELECT *
                      FROM personnes
                      ORDER BY prenom ASC """)
    return cursor.fetchall()


def update_user_acceuil(list_user):
    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute("""UPDATE personnes
                              SET email_perso = :email_perso, tel_perso = :tel_perso, adresse_perso = :adresse_perso
                              WHERE login = :login""", list_user)
        db.commit()
    except:
        db.rollback()


def update_user(list_user):
    db = get_db()
    cursor = db.cursor()
    try:
        # Désactiver les contraintes de clé étrangère
        cursor.execute("PRAGMA foreign_keys = OFF")

        cursor.execute("""UPDATE comptes
                                          SET login = :login_nouveau
                                          WHERE login = :login""", list_user)

        cursor.execute("""UPDATE personnes
                              SET nom = :nom, prenom = :prenom, naissance = :naissance, statut = :statut, email_uga = :email_uga, login = :login_nouveau, email_perso = :email_perso, tel_perso = :tel_perso, adresse_perso = :adresse_perso
                              WHERE login = :login""", list_user)

        db.commit()

        # Activer les contraintes de clé étrangère
        cursor.execute("PRAGMA foreign_keys = ON")

    except:
        db.rollback()


def del_user(login):
    db = get_db()
    cursor = db.cursor()

    try:
        # Désactiver les contraintes de clé étrangère
        cursor.execute("PRAGMA foreign_keys = OFF")

        cursor.execute("""DELETE FROM comptes WHERE login = :login""",
                       {'login': login})

        cursor.execute("""DELETE FROM personnes WHERE login = :login""",
                       {'login': login})
        db.commit()

        # Activer les contraintes de clé étrangère
        cursor.execute("PRAGMA foreign_keys = ON")

    except:
        db.rollback()


def add_user(user):
    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute("""INSERT INTO comptes (mdp,role,login)
                                      VALUES (:mdp, :role, :login)""", user)

        cursor.execute("""INSERT INTO personnes (nom,prenom,naissance,statut,email_uga,secu,login,email_perso,tel_perso,adresse_perso)
                              VALUES (:nom, :prenom, :naissance, :statut, :email_uga, :secu, :login, :email_perso, :tel_perso, :adresse_perso)""",
                       user)
        db.commit()

        return f"Ajout de {user['prenom']}"

    except sqlite3.Error as e:

        return f"Impossible d'ajouter {user['prenom']}"


def get_affectation_vue():
    cursor = get_db().cursor()
    cursor.execute("""SELECT *
                      FROM affectation_vue
                      ORDER BY nom ASC""")
    return cursor.fetchall()


def get_user_affectation_vue(num):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""SELECT * 
            FROM affectation_vue
            WHERE numero = :num""", {'num': num})
    return cursor.fetchone()


def del_affectation(num):
    db = get_db()
    cursor = db.cursor()

    try:
        # Désactiver les contraintes de clé étrangère
        cursor.execute("PRAGMA foreign_keys = OFF")

        cursor.execute("""DELETE FROM affectations WHERE numero = :num""",
                       {'num': num})

        db.commit()

        # Activer les contraintes de clé étrangère
        cursor.execute("PRAGMA foreign_keys = ON")

    except:
        db.rollback()


def update_affectation(list_user):
    db = get_db()
    cursor = db.cursor()
    try:

        cursor.execute("""UPDATE affectations
                                SET debut = :debut, fin = :fin, poste = :poste, service = :service, tel = :tel, tempstravail = :tempstravail
                                WHERE numero = :numero""", list_user)

        db.commit()

    except:
        db.rollback()


def get_service():
    cursor = get_db().cursor()
    cursor.execute("""SELECT *
                         FROM services""")
    return cursor.fetchall()


def add_affectation(user):
    db = get_db()
    cursor = db.cursor()
    try:
        # Désactiver les contraintes de clé étrangère
        cursor.execute("PRAGMA foreign_keys = OFF")
        cursor.execute("""INSERT INTO affectations (debut,fin,poste,secu,service,tel,tempstravail)
                              VALUES (:debut, :fin, :poste, :secu, :service, :tel, :tempstravail)""",
                       user)

        db.commit()
        # Activer les contraintes de clé étrangère
        cursor.execute("PRAGMA foreign_keys = ON")

        return f"Ajout de {user['secu']}"

    except sqlite3.Error as e:

        return f"Impossible d'ajouter {user['secu']}"


def get_services():
    cursor = get_db().cursor()
    cursor.execute("""SELECT *
                             FROM service_vue""")
    return cursor.fetchall()


def del_services(code):
    db = get_db()
    cursor = db.cursor()

    try:
        # Désactiver les contraintes de clé étrangère
        cursor.execute("PRAGMA foreign_keys = OFF")

        cursor.execute("""DELETE FROM structures WHERE code = :code""",
                       {'code': code})

        cursor.execute("""DELETE FROM services WHERE code = :code""",
                       {'code': code})

        db.commit()

        # Activer les contraintes de clé étrangère
        cursor.execute("PRAGMA foreign_keys = ON")

    except:
        db.rollback()


def get_service_vue(code):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""SELECT * 
            FROM service_vue
            WHERE code = :code""", {'code': code})
    return cursor.fetchone()


def get_structures():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""SELECT * 
                FROM structures""")
    return cursor.fetchall()


def update_services(service):
    db = get_db()
    cursor = db.cursor()
    try:

        # Désactiver les contraintes de clé étrangère
        cursor.execute("PRAGMA foreign_keys = OFF")

        cursor.execute("""UPDATE structures
                                        SET nom = :nom, code = :new_code_structures
                                        WHERE code = :code""", service)

        cursor.execute("""UPDATE services
                                SET nom = :nom, tel = :tel, email = :email, type = :type, code_structure = :new_code_structures
                                WHERE code = :code""", service)

        db.commit()

        # Activer les contraintes de clé étrangère
        cursor.execute("PRAGMA foreign_keys = ON")

    except:
        db.rollback()


def add_services(service):
    db = get_db()
    cursor = db.cursor()
    try:
        # Désactiver les contraintes de clé étrangère
        cursor.execute("PRAGMA foreign_keys = OFF")

        cursor.execute("""INSERT INTO services (nom,tel,email,type,code_structure,code)
                              VALUES (:nom, :tel, :email, :type, :code_structure, :code)""",
                       service)

        db.commit()
        # Activer les contraintes de clé étrangère
        cursor.execute("PRAGMA foreign_keys = ON")

        return f"Ajout de {service['nom']}"

    except sqlite3.Error as e:

        return f"Impossible d'ajouter {service['nom']}"


def check(login):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""SELECT login,mdp
            FROM comptes
            WHERE login = :login""", {'login': login})
    return cursor.fetchone()


def get_role(login):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""SELECT role
            FROM comptes
            WHERE login = :login""", {'login': login})
    return cursor.fetchone()

def get_user_nbrposte(login):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""SELECT count(poste) as nbrposte
            FROM affectations as A INNER JOIN personnes as P
            ON A.secu = P.secu
            WHERE login = :login""", {'login': login})
    return cursor.fetchone()
def get_user_compte(login):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""SELECT tempstravail,poste
            FROM affectations as A INNER JOIN personnes as P
            ON A.secu = P.secu
            WHERE login = :login""", {'login': login})
    return cursor.fetchall()

def get_login_num(num):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""SELECT P.login,A.secu
                FROM affectations as A INNER JOIN personnes as P
                ON A.secu = P.secu
                WHERE A.numero = :num""", {'num': num})
    return cursor.fetchone()



def get_nbrutilisateur(code):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""SELECT count(numero) as nbr
                    FROM affectations
                    WHERE service = :code""", {'code': code})
    return cursor.fetchone()

def get_rdm_user():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""SELECT *
                        FROM personnes""")
    return cursor.fetchone()