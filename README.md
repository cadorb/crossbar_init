# crossbar_init

Requirements : 

python libs > requirements.txt
mariadb or mysql 

CREATE DATABASE crossbar;
USE crossbar;

CREATE TABLE `click` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date_click` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=latin1;

CREATE USER 'user'@'localhost' IDENTIFIED BY 'user';
GRANT SELECT, INSERT ON crossbar.click TO 'user'@'localhost';
