PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "personnes"
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
INSERT OR IGNORE INTO personnes VALUES('265019390381521','Becker','Alexandrie','12-01-1981','15 Lot le Hameau du Neron, 38360 Sassenage','985842171','alexandrie.becker@gmail.com','alexandrie.becker@univ-grenoble-alpes.fr','beckeral','admin');
INSERT OR IGNORE INTO personnes VALUES('290017061594292','Brun','Clémence','17-07-1967','28 Rue la Valette, 38760 Varces-Allières-et-Risset','904065037','clemence.brun@yahoo.fr','clemence.brun@univ-grenoble-alpes.fr','brunclem','prof');
INSERT OR IGNORE INTO personnes VALUES('290011365138065','Carpentier','Hélène','06-12-1949','13 Rue du Maquis de Chambaran, 38210 Tullins','997772012','helene.carpentier@yahoo.fr','helene.carpentier@univ-grenoble-alpes.fr','carpenth','doctoran');
INSERT OR IGNORE INTO personnes VALUES('190052587722652','Delaunay-Leduc','Émile','26-06-1993','1552 Route sous le Mont, 38620 Voissant','727419361','emile.delaunay-leduc@hotmail.fr','emile.delaunay-leduc@univ-grenoble-alpes.fr','delaunae','mcf');
INSERT OR IGNORE INTO personnes VALUES('165101616380636','Dijoux','Thibaut','02-04-1975','5 Avenue Robert Huant, 38190 Villard-Bonnot','788089762','thibaut.dijoux@hotmail.fr','thibaut.dijoux@univ-grenoble-alpes.fr','dijouxth','mcf');
INSERT OR IGNORE INTO personnes VALUES('190063243662904','Gonzalez','Henri','19-02-1996','18 Rue des Camelias, 38280 Villette-d''Anthon','917810684','henri.gonzalez@yahoo.com','henri.gonzalez@univ-grenoble-alpes.fr','gonzaleh','prag');
INSERT OR IGNORE INTO personnes VALUES('190081028350647','Guyot-Gaillard','Marc','01-01-1948','14 Les Grandes Roches, 38460 Trept','948038357','marc.guyot-gaillard@yahoo.com','marc.guyot-gaillard@univ-grenoble-alpes.fr','guyotgam','mcf');
INSERT OR IGNORE INTO personnes VALUES('190084748939041','Hamon','Augustin','08-09-1966','21 Rue des Fours, 38190 Les Adrets','951174567','augustin.hamon@gmail.com','augustin.hamon@univ-grenoble-alpes.fr','hamonaug','admin');
INSERT OR IGNORE INTO personnes VALUES('290049867521858','Joubert','Charlotte','14-12-1994','6 Le Clos du Rivard, 38460 Trept','625925567','charlotte.joubert@orange.fr','charlotte.joubert@univ-grenoble-alpes.fr','joubertc','prof');
INSERT OR IGNORE INTO personnes VALUES('165123017574899','Labbe-Berger','Claude','10-05-1947','70 Chemin des Vieux, 38350 Susville','631197411','claude.labbe-berger@gmail.com','claude.labbe-berger@univ-grenoble-alpes.fr','labbebec','admin');
INSERT OR IGNORE INTO personnes VALUES('165089098147599','Le Laurent','Lucas','20-06-1949','90 Rue de la Pepiniere, 38190 Villard-Bonnot','724147769','lucas.le-laurent@yahoo.com','lucas.le-laurent@univ-grenoble-alpes.fr','lelaurel','admin');
INSERT OR IGNORE INTO personnes VALUES('165020542930447','Le Roux','Jean','27-04-1982','145 Rue du Curty, 38470 Têche','793040404','jean.le-roux@yahoo.fr','jean.le-roux@univ-grenoble-alpes.fr','lerouxje','prag');
INSERT OR IGNORE INTO personnes VALUES('165021561042195','Leveque','Alain','26-06-1949','14 Rue Raoul Follereau, 38180 Seyssins','423245444','alain.leveque@orange.fr','alain.leveque@univ-grenoble-alpes.fr','levequea','admin');
INSERT OR IGNORE INTO personnes VALUES('290112978027461','Leveque-Auger','Philippine','29-08-1944','64 Rue de Cartale, 38170 Seyssinet-Pariset','407001376','philippine.leveque-auger@hotmail.fr','philippine.leveque-auger@univ-grenoble-alpes.fr','levequep','admin');
INSERT OR IGNORE INTO personnes VALUES('265058386034892','Marques','Sylvie','05-05-1957','1113 Route de la Savane, 38290 Satolas-et-Bonce','958548692','sylvie.marques@hotmail.fr','sylvie.marques@univ-grenoble-alpes.fr','marquess','doctoran');
INSERT OR IGNORE INTO personnes VALUES('190107071609868','Moreau','Alexandre','17-11-1969','1726 Route de Bourgoin, 38510 Vézeronce-Curtin','742808832','alexandre.moreau@orange.fr','alexandre.moreau@univ-grenoble-alpes.fr','moreaual','prof');
INSERT OR IGNORE INTO personnes VALUES('165113042535155','Nguyen','Théophile','18-04-1970','17 Chemin du Vieux Sablonnières, 38460 Soleymieu','613840179','theophile.nguyen@orange.fr','theophile.nguyen@univ-grenoble-alpes.fr','nguyenth','prag');
INSERT OR IGNORE INTO personnes VALUES('290044850555531','Torres-Chauvet','Lucy','14-06-1975','201 Chemin de la Ville, 38260 Porte-des-Bonnevaux','930292334','lucy.torres-chauvet@hotmail.fr','lucy.torres-chauvet@univ-grenoble-alpes.fr','torrescl','doctoran');
CREATE TABLE IF NOT EXISTS "affectations"
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
INSERT OR IGNORE INTO affectations VALUES(0,'265019390381521','29-11-2009',NULL,'Technicien solutions de sécurité','iut1_mir','476413556',100);
INSERT OR IGNORE INTO affectations VALUES(1,'290017061594292','08-06-2018',NULL,'Enseignant','iut1_rt','476791705',50);
INSERT OR IGNORE INTO affectations VALUES(2,'290017061594292','08-06-2018',NULL,'Chercheur','modus','476382880',50);
INSERT OR IGNORE INTO affectations VALUES(3,'290011365138065','03-02-2017','03-02-2020','Doctorant','planeto','476382326',100);
INSERT OR IGNORE INTO affectations VALUES(4,'190052587722652','23-03-2017',NULL,'Enseignant','iut2_gea','476278840',50);
INSERT OR IGNORE INTO affectations VALUES(5,'190052587722652','23-03-2017',NULL,'Chercheur','planeto','476247834',50);
INSERT OR IGNORE INTO affectations VALUES(6,'165101616380636','05-02-2015',NULL,'Enseignant','iut2_gea','476893788',50);
INSERT OR IGNORE INTO affectations VALUES(7,'165101616380636','05-02-2015',NULL,'Chercheur','planeto','476937620',50);
INSERT OR IGNORE INTO affectations VALUES(8,'190063243662904','25-03-2016',NULL,'Enseignant','iut1_rt','476129299',100);
INSERT OR IGNORE INTO affectations VALUES(9,'190081028350647','11-04-2007',NULL,'Enseignant','iut1_rt','476168460',50);
INSERT OR IGNORE INTO affectations VALUES(10,'190081028350647','11-04-2007',NULL,'Chercheur','modus','476173695',50);
INSERT OR IGNORE INTO affectations VALUES(11,'190084748939041','01-03-2002',NULL,'Technicien Audiovisuel','dapi','476259683',100);
INSERT OR IGNORE INTO affectations VALUES(12,'290049867521858','05-12-2010',NULL,'Enseignant','iut1_rt','476576118',50);
INSERT OR IGNORE INTO affectations VALUES(13,'290049867521858','05-12-2010',NULL,'Chercheur','charm','476940137',50);
INSERT OR IGNORE INTO affectations VALUES(14,'165123017574899','16-01-2002',NULL,'Technicien Audiovisuel','dapi','476625739',100);
INSERT OR IGNORE INTO affectations VALUES(15,'165089098147599','17-10-2004',NULL,'Ingénieur pédagotique','dapi','476448400',100);
INSERT OR IGNORE INTO affectations VALUES(16,'165089098147599','17-09-2002','17-10-2004','Technicien Réseaux','iut1_mir','476490021',100);
INSERT OR IGNORE INTO affectations VALUES(17,'165020542930447','25-01-2013',NULL,'Enseignant','iut2_gea','476178992',100);
INSERT OR IGNORE INTO affectations VALUES(18,'165021561042195','03-09-2018',NULL,'Responsable des payes','rh','476230809',100);
INSERT OR IGNORE INTO affectations VALUES(19,'165021561042195','03-03-2016','03-09-2018','Ingénieur pédagotique','dapi','476916179',100);
INSERT OR IGNORE INTO affectations VALUES(20,'290112978027461','09-11-2001',NULL,'Ingénieur pédagotique','dapi','476145908',100);
INSERT OR IGNORE INTO affectations VALUES(21,'265058386034892','04-09-2019','04-09-2022','Doctorant','charm','476594261',100);
INSERT OR IGNORE INTO affectations VALUES(22,'190107071609868','15-11-2003',NULL,'Enseignant','iut2_gea','476521850',50);
INSERT OR IGNORE INTO affectations VALUES(23,'190107071609868','15-11-2003',NULL,'Chercheur','modus','476856566',50);
INSERT OR IGNORE INTO affectations VALUES(24,'165113042535155','26-03-2013',NULL,'Enseignant','iut2_gea','476506021',100);
INSERT OR IGNORE INTO affectations VALUES(25,'290044850555531','01-02-2020','01-02-2023','Doctorant','planeto','476904970',100);
CREATE TABLE IF NOT EXISTS "comptes"
(
    login VARCHAR(8)
        primary key,
    mdp   VARCHAR(128),
    role  VARCHAR(15) not null
);
INSERT OR IGNORE INTO comptes VALUES('brunclem','$2b$12$598cFMKShdHfHdG1xx056eKafZojt9/ToPB.Wm8iWnsm5.J3CkC8q','user');
INSERT OR IGNORE INTO comptes VALUES('joubertc','$2b$12$4Ey36WWRrLYur7bq.EEQ..9tfx5lwL3ZxrpyKDJmpFpieX33q/Rf6','user');
INSERT OR IGNORE INTO comptes VALUES('moreaual','$2b$12$3/QUeemRUKj69RemUSfFY.g8WyJ9d1IeMGYHDPH8GETVuYqqc4FKS','user');
INSERT OR IGNORE INTO comptes VALUES('guyotgam','$2b$12$gRq2IkSzSZLGtTjLRfOA6O9hIC2ZYH1FsVEqWAYDJo7xjydKvLjR6','user');
INSERT OR IGNORE INTO comptes VALUES('delaunae','$2b$12$dWwyQ1fm2jhpvmC1JcFZRO5ohNiHm6MMLV7ZVjZAMfeC.W0D7Z6Uy','user');
INSERT OR IGNORE INTO comptes VALUES('dijouxth','$2b$12$2P8UK78ImKNI.W/2/.AdjukkYd/piS1l7amFenl8WDoVBhjQr7kBG','user');
INSERT OR IGNORE INTO comptes VALUES('gonzaleh','$2b$12$Bwojr.s9fLHaSRoea7O/W.DQpvHZ1YPMDJsEUjlh.4OJe0ysmcrUu','user');
INSERT OR IGNORE INTO comptes VALUES('nguyenth','$2b$12$nXghPq3mVcpOH.bmSyl4sezn72kHBDEifSkoMhRuDsQZOXOl.VDQ2','user');
INSERT OR IGNORE INTO comptes VALUES('lerouxje','$2b$12$f/7.t35vieAfDnjeeM07.u1isHg/GmzOGfVznVplQz1pOH.v37XG2','user');
INSERT OR IGNORE INTO comptes VALUES('hamonaug','$2b$12$BI5n.rxR2pfOXcAleOAubuyiUFRd7DLyGF0k9PcD1T9m9Bgge.HqK','user');
INSERT OR IGNORE INTO comptes VALUES('lelaurel','$2b$12$sdRL.K1.OENfU51.ktIMGe7UJMyefZlppApxkdhLsnFeQBi3dFS5S','user');
INSERT OR IGNORE INTO comptes VALUES('beckeral','$2b$12$W3evSOnfG0793bSQ7i.xOecjIHUSqvvwFwIlrMpXBWjYWsNjTXj1.','user');
INSERT OR IGNORE INTO comptes VALUES('levequea','$2b$12$anTpxcknLi1LYsng5G6PXuL836JcK4a62yIWTJvxVaRF4w5Xx4g1C','rh');
INSERT OR IGNORE INTO comptes VALUES('levequep','$2b$12$fE5pWzWqhokyx383STypSOSPTFHDw0gToiBG7qD7KbjyonsCHNceW','user');
INSERT OR IGNORE INTO comptes VALUES('labbebec','$2b$12$KZM.Y.tu9sr9fs52aH0gTON/QDD3.pE4tjO9uRLmnD8CVvM5BM0o2','user');
INSERT OR IGNORE INTO comptes VALUES('carpenth','$2b$12$TDtQrMller.rPi4GL.N.WuGIAFLTT.MfZOzxz1fuWVQjviXeZQRxm','user');
INSERT OR IGNORE INTO comptes VALUES('marquess','$2b$12$YztcKjN.XxZ3aUSVX7iKuOOqALKGSC83ilPVNVuwv3wHPeq/0L80e','user');
INSERT OR IGNORE INTO comptes VALUES('torrescl','$2b$12$tLLqleGpxXFqyOqq0Jxg0eyTW6L1YDRO3hSgSi3eklCUQlXo8jcM2','user');
INSERT OR IGNORE INTO comptes VALUES('admin','$2b$12$0T.6Ojr5siqUyMz/jsesneg9RTDYcAIzwx5Wp0ONvlr4OwvERUrtu','admin');
CREATE TABLE IF NOT EXISTS "services"
(
    code           VARCHAR(6)
        primary key,
    nom            VARCHAR(50),
    tel            VARCHAR(10),
    email          VARCHAR(100),
    type           VARCHAR(15),
    code_structure VARCHAR(6)
        constraint code_structure
            references structures
);
INSERT OR IGNORE INTO services VALUES('dapi','Direction d’Appui à la Pédagogie et à l’Innovation','476232888','dapi@univ-grenoble-alpes.fr','administration','uga_sg');
INSERT OR IGNORE INTO services VALUES('iut2_gea','Département Gestion des Entreprises et Administration','476436951','iut2.gea@univ-grenoble-alpes.fr','enseignement','iut2');
INSERT OR IGNORE INTO services VALUES('iut1_rt','Département R&T','476514858','iut1.rt@univ-grenoble-alpes.fr','enseignement','iut1');
INSERT OR IGNORE INTO services VALUES('charm','Equipe Charm','476586905','ipag.charm@univ-grenoble-alpes.fr','recherche','ipag');
INSERT OR IGNORE INTO services VALUES('modus','Equipe MODUS','476063327','gipsalab.modus@univ-grenoble-alpes.fr','recherche','gipsalab');
INSERT OR IGNORE INTO services VALUES('planeto','Equipe Planéto','476435845','ipag.planeto@univ-grenoble-alpes.fr','recherche','ipag');
INSERT OR IGNORE INTO services VALUES('iut1_mir','MIR','476562017','iut1.mir@univ-grenoble-alpes.fr','administration','iut1');
INSERT OR IGNORE INTO services VALUES('rh','Service des Ressources Humaines','476903052','rh@univ-grenoble-alpes.fr','administration','uga_sg');
CREATE TABLE IF NOT EXISTS "structures"
(
    code VARCHAR(6)
        primary key,
    nom  VARCHAR(100) not null
);
INSERT OR IGNORE INTO structures VALUES('uga_sg','Services Généraux de l''UGA');
INSERT OR IGNORE INTO structures VALUES('iut2','IUT 2');
INSERT OR IGNORE INTO structures VALUES('iut1','IUT 1');
INSERT OR IGNORE INTO structures VALUES('ipag','Institut de planétologie et d''astrophysique de Grenoble');
INSERT OR IGNORE INTO structures VALUES('gipsalab','Laboratoire Gipsa Lab');
COMMIT;

CREATE view if not exists "affectation_vue" AS
Select P.email_uga, P.login, P.nom, P.prenom, A.debut, A.fin, A.poste, A.service, A.tel, A.tempstravail, A.Secu, A.numero, S.nom as "nom_service"
FROM personnes AS P INNER JOIN affectations AS A
ON P.secu = A.secu
INNER JOIN services as S
ON S.code = A.service;

CREATE view if not exists "service_vue" AS
SELECT S.nom, S.tel, S.email, S.type, S.code_structure, S.code, ST.nom as "nom_structures"
FROM services AS S INNER JOIN structures AS ST
ON S.code_structure = ST.code;