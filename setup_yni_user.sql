-- sets up a new user for yni_db
CREATE DATABASE IF NOT EXISTS yni_db;

CREATE USER IF NOT EXISTS 'yni_dev'@'localhost' IDENTIFIED BY 'yni_dev_pwd';

GRANT ALL PRIVILEGES ON yni_db.* TO 'yni_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'yni_dev'@'localhost';