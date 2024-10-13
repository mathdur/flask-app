PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

CREATE TABLE "personnes"
(
    secu          VARCHAR(15)
        primary key,
    nom           VARCHAR(50) not null,
    prenom        VARCHAR(50) not null,
    naissance     date,
    adresse_perso text,
    tel_perso     VARCHAR(10),
    email_perso   VARCHAR(100),
    email_uga     VARCHAR(100),
    login         VARCHAR(8)
        constraint login
            references comptes,
    statut        VARCHAR(8)
);

INSERT INTO personnes VALUES('265019390381521','Becker','Alexandrie','12-01-1981','15 Lot le Hameau du Neron, 38360 Sassenage','985842171','alexandrie.becker@gmail.com','alexandrie.becker@univ-grenoble-alpes.fr','beckeral','admin');
INSERT INTO personnes VALUES('290017061594292','Brun','Clémence','17-07-1967','28 Rue la Valette, 38760 Varces-Allières-et-Risset','904065037','clemence.brun@yahoo.fr','clemence.brun@univ-grenoble-alpes.fr','brunclem','prof');
INSERT INTO personnes VALUES('290011365138065','Carpentier','Hélène','06-12-1949','13 Rue du Maquis de Chambaran, 38210 Tullins','997772012','helene.carpentier@yahoo.fr','helene.carpentier@univ-grenoble-alpes.fr','carpenth','doctoran');
INSERT INTO personnes VALUES('190052587722652','Delaunay-Leduc','Émile','26-06-1993','1552 Route sous le Mont, 38620 Voissant','727419361','emile.delaunay-leduc@hotmail.fr','emile.delaunay-leduc@univ-grenoble-alpes.fr','delaunae','mcf');
INSERT INTO personnes VALUES('165101616380636','Dijoux','Thibaut','02-04-1975','5 Avenue Robert Huant, 38190 Villard-Bonnot','788089762','thibaut.dijoux@hotmail.fr','thibaut.dijoux@univ-grenoble-alpes.fr','dijouxth','mcf');
INSERT INTO personnes VALUES('190063243662904','Gonzalez','Henri','19-02-1996','18 Rue des Camelias, 38280 Villette-d''Anthon','917810684','henri.gonzalez@yahoo.com','henri.gonzalez@univ-grenoble-alpes.fr','gonzaleh','prag');
INSERT INTO personnes VALUES('190081028350647','Guyot-Gaillard','Marc','01-01-1948','14 Les Grandes Roches, 38460 Trept','948038357','marc.guyot-gaillard@yahoo.com','marc.guyot-gaillard@univ-grenoble-alpes.fr','guyotgam','mcf');
INSERT INTO personnes VALUES('190084748939041','Hamon','Augustin','08-09-1966','21 Rue des Fours, 38190 Les Adrets','951174567','augustin.hamon@gmail.com','augustin.hamon@univ-grenoble-alpes.fr','hamonaug','admin');
INSERT INTO personnes VALUES('290049867521858','Joubert','Charlotte','14-12-1994','6 Le Clos du Rivard, 38460 Trept','625925567','charlotte.joubert@orange.fr','charlotte.joubert@univ-grenoble-alpes.fr','joubertc','prof');
INSERT INTO personnes VALUES('165123017574899','Labbe-Berger','Claude','10-05-1947','70 Chemin des Vieux, 38350 Susville','631197411','claude.labbe-berger@gmail.com','claude.labbe-berger@univ-grenoble-alpes.fr','labbebec','admin');
INSERT INTO personnes VALUES('165089098147599','Le Laurent','Lucas','20-06-1949','90 Rue de la Pepiniere, 38190 Villard-Bonnot','724147769','lucas.le-laurent@yahoo.com','lucas.le-laurent@univ-grenoble-alpes.fr','lelaurel','admin');
INSERT INTO personnes VALUES('165020542930447','Le Roux','Jean','27-04-1982','145 Rue du Curty, 38470 Têche','793040404','jean.le-roux@yahoo.fr','jean.le-roux@univ-grenoble-alpes.fr','lerouxje','prag');
INSERT INTO personnes VALUES('165021561042195','Leveque','Alain','26-06-1949','14 Rue Raoul Follereau, 38180 Seyssins','423245444','alain.leveque@orange.fr','alain.leveque@univ-grenoble-alpes.fr','levequea','admin');
INSERT INTO personnes VALUES('290112978027461','Leveque-Auger','Philippine','29-08-1944','64 Rue de Cartale, 38170 Seyssinet-Pariset','407001376','philippine.leveque-auger@hotmail.fr','philippine.leveque-auger@univ-grenoble-alpes.fr','levequep','admin');
INSERT INTO personnes VALUES('265058386034892','Marques','Sylvie','05-05-1957','1113 Route de la Savane, 38290 Satolas-et-Bonce','958548692','sylvie.marques@hotmail.fr','sylvie.marques@univ-grenoble-alpes.fr','marquess','doctoran');
INSERT INTO personnes VALUES('190107071609868','Moreau','Alexandre','17-11-1969','1726 Route de Bourgoin, 38510 Vézeronce-Curtin','742808832','alexandre.moreau@orange.fr','alexandre.moreau@univ-grenoble-alpes.fr','moreaual','prof');
INSERT INTO personnes VALUES('165113042535155','Nguyen','Théophile','18-04-1970','17 Chemin du Vieux Sablonnières, 38460 Soleymieu','613840179','theophile.nguyen@orange.fr','theophile.nguyen@univ-grenoble-alpes.fr','nguyenth','prag');
INSERT INTO personnes VALUES('290044850555531','Torres-Chauvet','Lucy','14-06-1975','201 Chemin de la Ville, 38260 Porte-des-Bonnevaux','930292334','lucy.torres-chauvet@hotmail.fr','lucy.torres-chauvet@univ-grenoble-alpes.fr','torrescl','doctoran');

CREATE TABLE "affectations"
(
    numero       INTEGER
        primary key,
    secu         VARCHAR(15)
        constraint secu
            references personnes,
    debut        date not null,
    fin          date,
    poste        VARCHAR(100),
    service      VARCHAR(100)
        constraint service
            references services,
    tel          VARCHAR(10),
    tempstravail int
);

INSERT INTO affectations VALUES(0,'265019390381521','29-11-2009',NULL,'Technicien solutions de sécurité','iut1_mir','476413556',100);
INSERT INTO affectations VALUES(1,'290017061594292','08-06-2018',NULL,'Enseignant','iut1_rt','476791705',50);
INSERT INTO affectations VALUES(2,'290017061594292','08-06-2018',NULL,'Chercheur','modus','476382880',50);
INSERT INTO affectations VALUES(3,'290011365138065','03-02-2017','03-02-2020','Doctorant','planeto','476382326',100);
INSERT INTO affectations VALUES(4,'190052587722652','23-03-2017',NULL,'Enseignant','iut2_gea','476278840',50);
INSERT INTO affectations VALUES(5,'190052587722652','23-03-2017',NULL,'Chercheur','planeto','476247834',50);
INSERT INTO affectations VALUES(6,'165101616380636','05-02-2015',NULL,'Enseignant','iut2_gea','476893788',50);
INSERT INTO affectations VALUES(7,'165101616380636','05-02-2015',NULL,'Chercheur','planeto','476937620',50);
INSERT INTO affectations VALUES(8,'190063243662904','25-03-2016',NULL,'Enseignant','iut1_rt','476129299',100);
INSERT INTO affectations VALUES(9,'190081028350647','11-04-2007',NULL,'Enseignant','iut1_mir','476029469',50);
INSERT INTO affectations VALUES(10,'190084748939041','05-05-2009','01-06-2014','Technicien informatique','iut1_mir','476182970',100);
INSERT INTO affectations VALUES(11,'290049867521858','01-01-2022',NULL,'Doctorant','modus','476873540',100);
INSERT INTO affectations VALUES(12,'165123017574899','05-04-2015',NULL,'Enseignant','iut1_rt','476204284',50);
INSERT INTO affectations VALUES(13,'165089098147599','15-11-2010',NULL,'Enseignant','iut2_gea','476156096',50);
INSERT INTO affectations VALUES(14,'165020542930447','25-08-2015',NULL,'Technicien solutions de sécurité','iut2_gea','476411030',50);
INSERT INTO affectations VALUES(15,'165021561042195','15-11-2010',NULL,'Enseignant','iut1_mir','476098586',50);
INSERT INTO affectations VALUES(16,'290112978027461','29-08-2020','28-08-2022','Enseignant','iut2_gea','476972665',50);
INSERT INTO affectations VALUES(17,'265058386034892','05-02-2015',NULL,'Enseignant','iut2_gea','476195818',50);
INSERT INTO affectations VALUES(18,'190107071609868','29-08-2015',NULL,'Enseignant','iut1_rt','476529041',50);
INSERT INTO affectations VALUES(19,'165113042535155','01-01-2020',NULL,'Enseignant','iut2_gea','476859024',50);
INSERT INTO affectations VALUES(20,'290044850555531','29-08-2016','30-12-2018','Doctorant','planeto','476271534',100);

CREATE TABLE "services"
(
    id    VARCHAR(15)
        primary key,
    nom   VARCHAR(100) not null
);

INSERT INTO services VALUES('iut1_rt','IUT 1 - Réseaux et télécommunications');
INSERT INTO services VALUES('iut1_mir','IUT 1 - Méthodes informatiques et réseaux');
INSERT INTO services VALUES('iut2_gea','IUT 2 - Gestion des entreprises et des administrations');
INSERT INTO services VALUES('modus','Modélisation et simulation');
INSERT INTO services VALUES('planeto','Planétologie');

CREATE VIEW "affectations_vues" AS
SELECT
    a.secu,
    p.nom,
    p.prenom,
    p.naissance,
    a.debut,
    a.fin,
    a.poste,
    a.service,
    a.tel,
    a.tempstravail
FROM
    affectations a
JOIN
    personnes p ON a.secu = p.secu;

COMMIT;
