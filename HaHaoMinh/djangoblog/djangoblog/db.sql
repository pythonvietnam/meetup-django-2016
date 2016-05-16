CREATE DATABASE djangoblog;
CREATE USER 'minhha' @'localhost' IDENTIFIED BY 'haminh';
GRANT ALL PRIVILEGES ON * .* TO 'minhha'@'localhost' WITH GRANT OPTION;
SELECT
  host,
  user,
  password,
  Grant_priv,
  Super_priv
FROM mysql.user;
UPDATE mysql.user SET Grant_priv = 'Y', Super_priv = 'Y' WHERE User = 'root';
FLUSH PRIVILEGES;

DROP DATABASE djangoblog;
DROP USER 'minhha'@'localhost';
SET SQL_SAFE_UPDATES=0;

