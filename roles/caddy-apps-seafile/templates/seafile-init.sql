-- official seafile sql scripts
-- https://github.com/haiwen/seafile-server/tree/master/scripts/sql/mysql
-- https://github.com/haiwen/seahub/blob/4610299fabfeef4b45ce14aeb57fb19771224319/sql/mysql.sql#L4


-- -- only create it if using it manually, during first init seafile will create it with a different password
-- create user IF NOT EXISTS 'seafile'@'%.%.%.%' identified by '{{ mariadb_seafile_user_passwd }}';
ALTER USER IF EXISTS 'seafile'@'%.%.%.%' IDENTIFIED BY '{{ mariadb_seafile_user_passwd }}';


-- create database IF NOT EXISTS `ccnet_db` character set = 'utf8';
-- create database IF NOT EXISTS `seafile_db` character set = 'utf8';
-- create database IF NOT EXISTS `seahub_db` character set = 'utf8';

-- GRANT ALL PRIVILEGES ON `ccnet_db`.* to 'seafile'@'%.%.%.%';
-- GRANT ALL PRIVILEGES ON `seafile_db`.* to 'seafile'@'%.%.%.%';
-- GRANT ALL PRIVILEGES ON `seahub_db`.* to 'seafile'@'%.%.%.%';

-- FLUSH PRIVILEGES;
