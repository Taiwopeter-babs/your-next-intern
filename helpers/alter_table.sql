-- adds a new column
USE yni_db;
-- ALTER TABLE company_intern
-- MODIFY `date_applied` DATE NOT NULL DEFAULT (CURRENT_DATE());
ALTER TABLE companies
ADD COLUMN `password` VARCHAR(256) NOT NULL AFTER `email`;