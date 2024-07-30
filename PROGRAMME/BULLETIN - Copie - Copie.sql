
CREATE DATABASE BULLETIN;
USE BULLETIN;

CREATE TABLE Eleve(
    id_eleve INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(20) NOT NULL ,
    prenom VARCHAR(30) NOT NULL ,
    sexe VARCHAR(20),
    naissance VARCHAR(40),
    lieu VARCHAR(30) NOT NULL,
    numero VARCHAR(50) NOT NULL ,
    statut VARCHAR(20) NOT NULL,
    classe VARCHAR(10) NOT NULL,
    anne VARCHAR(20) NOT NULL,
    decou VARCHAR(20) NOT NULL)ENGINE=INNODB;

CREATE TABLE Matiere(
    id_mat INT NOT NULL,
    nom_mat VARCHAR(30) NOT NULL,
    moyclass INT NOT NULL,
    notecompo INT NOT NULL,
    moygen INT NOT NULL,
    coef INT NOT NULL,
    rang INT NOT NULL,
    prof_mat VARCHAR(30) NOT NULL,
    appreciation VARCHAR(40) NOT NULL,
    id_eleve INT NOT NULL,
    CONSTRAINT el_fk FOREIGN KEY(id_eleve) REFERENCES Eleve(id_eleve))ENGINE=INNODB;

CREATE TABLE Moyengen(
    id_moyenne INT NOT NULL,
    moyennegenerale INT NOT NULL,
    id_eleve INT NOT NULL,
    CONSTRAINT el2_fk FOREIGN KEY(id_eleve) REFERENCES Eleve(id_eleve))ENGINE=INNODB   