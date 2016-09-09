# crossbar_init
<br>
Requirements : <br>
<br>
python libs > requirements.txt<br>
mariadb or mysql <br>
<br>
CREATE DATABASE crossbar;<br>
USE crossbar;<br>
<br>
CREATE TABLE `click` (<br>
  `id` int(11) NOT NULL AUTO_INCREMENT,<br>
  `date_click` datetime DEFAULT NULL,<br>
  PRIMARY KEY (`id`)<br>
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=latin1;<br>
<br>
CREATE USER 'user'@'localhost' IDENTIFIED BY 'user';<br>
GRANT SELECT, INSERT ON crossbar.click TO 'user'@'localhost';<br>
